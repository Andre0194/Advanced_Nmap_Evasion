# OS-Specific Nmap Port Scanner - `mrphysiquee` Tool 6

This tool uses Python to select the most suitable Nmap scan depending on the target operating system — Android or Windows.

## ⚙️ Features

- Detects target OS type via user input
- Uses aggressive scans for Windows
- Uses stealthy scans for Android
- Automates `nmap` flags

## 🧰 Requirements

- Python 3
- Nmap installed

Install Nmap:
```bash
sudo apt update && sudo apt install nmap



🚀 Usage
python3 scanner.py

🛡️ Legal Disclaimer
This tool is for educational and authorized penetration testing only. Always obtain permission before scanning.
