# 📊 Live Log Monitoring Dashboard

A real-time log monitoring dashboard built with **Python (Flask)** that simulates live server logs, extracts useful information using **Regular Expressions (Regex)**, and displays statistics through a responsive web dashboard with light/dark mode. The project is containerized with **Docker**, deployed through a **Jenkins CI/CD pipeline**, and includes a **GitHub Actions** workflow for automated builds and health checks. Critical events trigger real-time alerts via **AWS SNS**.

---

## 🚀 Features

- 📄 Live log generation (simulated server logs)
- 🔍 Regex-based parsing for:
  - IP Addresses
  - Email Addresses
  - Error Events
- 📊 Real-time dashboard with light/dark mode toggle
- 🔔 Real-time critical event alerts via AWS SNS
- 🌐 REST API for log data
- 🐳 Docker support
- ⚙️ Jenkins CI/CD pipeline
- ⚙️ GitHub Actions Continuous Integration
- ❤️ Health Check endpoint

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML / CSS / JavaScript
- Regular Expressions (Regex)
- Docker
- Jenkins
- GitHub Actions
- AWS SNS (boto3)

---

## 📂 Project Structure

```
.
├── app.py
├── templates/
│   └── dashboard.html
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .github/
│   └── workflows/
└── README.md
```

---

## ⚡ Getting Started

### Clone the Repository

```
git clone https://github.com/Yash-Sonii/log-dashboard.git
cd log-dashboard
```

### Create Virtual Environment

```
python -m venv venv
```

### Activate Environment

Linux / macOS
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the Application

```
python app.py
```

Open your browser:
```
http://localhost:5000
```

---

## 🐳 Run with Docker

```
docker build -t log-dashboard .
docker run -p 5000:5000 log-dashboard
```

---

## ⚙️ CI/CD Pipeline

**GitHub Actions** builds the Docker image, runs the container, and hits `/health` on every push to `main`.

**Jenkins** runs a full pipeline (Checkout → Build → Run → Wait → Verify → Cleanup) against a local Jenkins server. Two real issues encountered and fixed while wiring this up:

- **Docker permission denied**: the `jenkins` system user wasn't part of the `docker` group, blocking access to `docker.sock`. Fixed with `usermod -aG docker jenkins` and a Jenkins service restart.
- **Health check failing right after container start**: the container needed a moment to bind the port before `curl /health` would succeed. Fixed by adding a short wait stage between the run and verify steps.

---

## 🔔 Real-Time Alerts (AWS SNS)

When the regex parser detects a critical event (`ERROR`, `FAILED`, `DENIED`, `CRITICAL`), the app publishes a message to an AWS SNS topic, which sends a real-time email alert — with a cooldown to avoid alert spam.

---

## 🔗 API Endpoints

| Endpoint    | Description                     |
| ----------- | -------------------------------- |
| `/`         | Dashboard                        |
| `/api/logs` | Returns log data and statistics  |
| `/health`   | Health check endpoint            |

---

## 📈 What This Project Demonstrates

- Flask Web Development
- REST API Design
- Regular Expressions (Regex)
- Multi-threading
- Docker Containerization
- Jenkins CI/CD Pipeline (with real debugging: permissions, timing issues)
- GitHub Actions CI
- AWS SNS Integration (boto3)
- DevOps Fundamentals

---

## 🎯 Future Improvements

- Database integration (SQLite/PostgreSQL)
- Kubernetes deployment
- Authentication
- Real log ingestion
- Log filtering and search
- Charts and analytics

---

## 👨‍💻 Author

**Yash Soni**

GitHub: https://github.com/Yash-Sonii

LinkedIn: https://www.linkedin.com/in/yash-soni-273464298/

---

⭐ If you found this project useful, consider giving it a star!