# 🛡️ NetSentry v1.0
### Smart Network Security Auditor

NetSentry is a Python-based network security auditing tool designed to discover network devices, scan TCP ports, detect running services, analyze potential security risks, and generate PDF security reports.

## 🚀 Features

- Network Discovery
- TCP Port Scanning
- Service Detection
- Rule-Based Risk Analysis
- Flask Web Dashboard
- Security Statistics
- PDF Security Report Generation

## 🛠️ Technologies

- Python
- Nmap
- Flask
- ReportLab
- HTML & CSS
- Kali Linux

## 📁 Project Structure

```text
NetSentry/
├── app.py
├── main.py
├── scanner/
├── reports/
├── templates/
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sreedevs224-byte/NetSentry.git
```

Enter the project:

```bash
cd NetSentry
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Nmap:

```bash
sudo apt install nmap
```

## ▶️ Usage

Run command-line version:

```bash
python main.py
```

Run web dashboard:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

Enter an authorized private IP address to analyze the network.

## 📊 Security Analysis

NetSentry provides preliminary security risk indicators based on port states and predefined rules.

These indicators are not confirmed vulnerability findings.

## 🔐 Disclaimer

This project is intended for educational purposes and authorized security testing only.

Only scan networks and devices that you own or have explicit permission to test.

## 👨‍💻 Author

Developed as a cybersecurity learning and portfolio project.

**Project:** NetSentry v1.0
