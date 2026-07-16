from flask import Flask, jsonify, render_template
import re
import threading
import time
import random
from collections import deque
from datetime import datetime

app = Flask(__name__)

LOG_BUFFER = deque(maxlen=50)
STATS = {"total_lines": 0, "total_ips": 0, "total_emails": 0, "total_errors": 0}
LOCK = threading.Lock()

IP_REGEX = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
EMAIL_REGEX = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
ERROR_REGEX = re.compile(r'\b(ERROR|FAILED|DENIED|CRITICAL)\b', re.IGNORECASE)


def parse_line(line: str) -> dict:
    ips = IP_REGEX.findall(line)
    emails = EMAIL_REGEX.findall(line)
    is_error = bool(ERROR_REGEX.search(line))

    with LOCK:
        STATS["total_lines"] += 1
        STATS["total_ips"] += len(ips)
        STATS["total_emails"] += len(emails)
        if is_error:
            STATS["total_errors"] += 1

    entry = {
        "timestamp": datetime.utcnow().strftime("%H:%M:%S"),
        "raw": line,
        "ips": ips,
        "emails": emails,
        "is_error": is_error,
    }
    with LOCK:
        LOG_BUFFER.appendleft(entry)
    return entry


SAMPLE_EVENTS = [
    "User login from {ip} succeeded",
    "User login from {ip} FAILED - invalid password",
    "Password reset requested for {email}",
    "Connection from {ip} DENIED - blocked IP range",
    "New signup: {email} from {ip}",
    "CRITICAL - database connection lost from {ip}",
    "API request processed for {email}",
    "ERROR - timeout connecting to {ip}",
]


def random_ip():
    return f"{random.randint(10,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"


def random_email():
    users = ["alice", "bob", "admin", "priya", "yash", "system"]
    domains = ["company.com", "gmail.com", "corp.io"]
    return f"{random.choice(users)}@{random.choice(domains)}"


def log_generator():
    while True:
        template = random.choice(SAMPLE_EVENTS)
        line = template.format(ip=random_ip(), email=random_email())
        parse_line(line)
        time.sleep(random.uniform(1.0, 2.5))


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/logs")
def api_logs():
    with LOCK:
        return jsonify({
            "stats": dict(STATS),
            "logs": list(LOG_BUFFER),
        })


if __name__ == "__main__":
    threading.Thread(target=log_generator, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
