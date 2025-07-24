# OS-Aware Nmap Port Scanner - `mrphysiquee` Tool 4

This Python script adapts Nmap scanning based on the selected target OS (Android or Windows). Ideal for quick recon in internal networks or labs.

## 🔧 Requirements

- Python 3
- Nmap (`sudo apt install nmap`)

## 📋 Features

- Automatically adjusts ports based on OS:
  - **Android:** 5555, 8080, 12345
  - **Windows:** 21, 22, 80, 139, 445, 3389
- Fast SYN scan
- Clean user prompts

## 🚀 Usage

```bash
python3 os_scan.py


⚠️ Note
Use only for educational or authorized penetration testing purposes.
