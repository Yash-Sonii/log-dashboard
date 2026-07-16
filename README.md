# Live Log Monitoring Dashboard

A Flask application that ingests log lines, parses them in real time to
extract IP addresses, email addresses, and error markers using regex, and
streams the results to a live-updating web dashboard.

A background thread simulates incoming log traffic (standing in for a real
log source such as an app server or syslog feed), so the dashboard updates
continuously. The frontend polls `/api/logs` every 2 seconds to refresh
stats and the live log table.

## Endpoints

- `GET /` — the dashboard UI
- `GET /health` — health check (used by Docker/CI/load balancers)
- `GET /api/logs` — JSON of current stats + last 50 parsed log entries

## Run locally

```bash
docker build -t log-dashboard:1.0 .
docker run -p 5000:5000 log-dashboard:1.0
```

Then open http://localhost:5000

## Run without Docker

```bash
pip install -r requirements.txt
python app.py
```

## CI/CD

Every push triggers a GitHub Actions workflow that builds the Docker image,
starts the container, and verifies it responds on `/health`.

## Architecture

```
Simulated log source (background thread)
        │
        ▼
   Regex parser (IP / email / error detection)
        │
        ▼
  In-memory buffer (last 50 entries) + running stats
        │
        ▼
   /api/logs endpoint (JSON)
        │
        ▼
  Browser polls every 2s → live dashboard
```
