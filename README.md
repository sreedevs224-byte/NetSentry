# 🛡️ NetSentry – Smart Network Security Auditor

NetSentry is a Python-based network security auditing tool designed to discover devices, scan common TCP ports, identify services, analyze basic security risks, and generate professional PDF security reports.

## 🚀 Features

- Network Discovery
- TCP Port Scanning
- Service Detection
- Rule-Based Risk Analysis
- Flask Web Dashboard
- Security Statistics
- PDF Security Report Generation

## 🛠️ Technologies Used

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
│   ├── network_discovery.py
│   ├── port_scanner.py
│   ├── service_detection.py
│   └── risk_analyzer.py
├── reports/
│   ├── __init__.py
│   └── pdf_report.py
├── templates/
│   └── index.html
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd NetSentry
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Nmap is installed:

```bash
sudo apt install nmap
```

## ▶️ Run NetSentry

### Command-line interface

```bash
python main.py
```

### Web dashboard

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

Enter an authorized private IP address to perform a scan.

## 📊 Security Analysis

NetSentry provides preliminary risk indicators based on port states and predefined rules.

**Note:** These indicators are not confirmed vulnerability findings. Open ports do not automatically mean a system is vulnerable.

## 🔐 Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan networks and devices that you own or have explicit permission to test.

## 👨‍💻 Author

Developed as a cybersecurity learning and portfolio project.

**Project:** NetSentry v1.0
