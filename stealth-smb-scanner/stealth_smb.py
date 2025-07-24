import subprocess
import argparse

def stealth_smb_scan(target):
    print(f"\n[+] Starting stealthy SMB scan on {target}...\n")
    
    command = [
        "nmap",
        "-sS",         # TCP SYN scan
        "-Pn",         # Skip host discovery
        "-p", "445",   # Target port for SMB
        "--script", "smb-os-discovery.nse,smb-enum-shares.nse",
        "--open",      # Show only open ports
        "--max-rate", "200",  # Limit packet rate
        target
    ]

    subprocess.run(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stealthy SMB Scanner using Nmap")
    parser.add_argument("target", help="Target IP address or hostname")
    args = parser.parse_args()
    stealth_smb_scan(args.target)
