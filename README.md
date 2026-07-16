# 📊 Live Log Monitoring Dashboard

A real-time log monitoring dashboard built with **Python (Flask)** that simulates live server logs, extracts useful information using **Regular Expressions (Regex)**, and displays statistics through a responsive web dashboard. The project is containerized with **Docker** and includes a **GitHub Actions CI** workflow for automated builds and health checks.

---

## 🚀 Features

- 📄 Live log generation (simulated server logs)
- 🔍 Regex-based parsing for:
  - IP Addresses
  - Email Addresses
  - Error Events
- 📊 Real-time dashboard
- 🌐 REST API for log data
- 🐳 Docker support
- ⚙️ GitHub Actions Continuous Integration
- ❤️ Health Check endpoint

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML
- CSS
- JavaScript
- Regular Expressions (Regex)
- Docker
- GitHub Actions

---

## 📂 Project Structure

```
.
├── app.py
├── templates/
│   └── dashboard.html
├── static/
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
└── README.md
```

---

## ⚡ Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

## 🐳 Run with Docker

Build the Docker image

```bash
docker build -t log-dashboard .
```

Run the container

```bash
docker run -p 5000:5000 log-dashboard
```

---

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Dashboard |
| `/api/logs` | Returns log data and statistics |
| `/health` | Health check endpoint |

---

## 📈 What This Project Demonstrates

- Flask Web Development
- REST API Design
- Regular Expressions (Regex)
- Multi-threading
- Docker Containerization
- GitHub Actions CI
- DevOps Fundamentals

---

## 🎯 Future Improvements

- Database integration (SQLite/PostgreSQL)
- Kubernetes deployment
- Jenkins pipeline
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
