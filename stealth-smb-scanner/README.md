# Stealth SMB Scanner - `mrphysiquee` Tool 4

A Python wrapper that stealthily scans a target host for SMB shares and OS details using Nmap NSE scripts.

## 🔧 Requirements

- Python 3
- Nmap with NSE scripts
- Linux (recommended for terminal and permissions)

## ⚙️ Features

- Stealthy SYN scan (`-sS`)
- Skips host discovery (`-Pn`)
- Targets port 445 (SMB)
- Uses Nmap scripts:
  - `smb-os-discovery.nse`
  - `smb-enum-shares.nse`
- Evades basic IDS/IPS using rate limiting (`--max-rate`)

## 🚀 Usage

```bash
python3 stealth_smb.py 192.168.1.100
