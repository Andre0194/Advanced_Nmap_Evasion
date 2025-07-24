#!/usr/bin/env python3

import os
import platform
import subprocess

def scan_android(target_ip):
    print(f"[+] Running Android-suggested Nmap scan on {target_ip}")
    cmd = f"nmap -sS -sV -p 1-1000 {target_ip}"
    subprocess.call(cmd, shell=True)

def scan_windows(target_ip):
    print(f"[+] Running Windows-suggested Nmap scan on {target_ip}")
    cmd = f"nmap -sS -T4 -A -Pn {target_ip}"
    subprocess.call(cmd, shell=True)

def main():
    target_ip = input("Enter target IP: ").strip()
    os_type = input("Target OS (android/windows): ").lower()

    if os_type == "android":
        scan_android(target_ip)
    elif os_type == "windows":
        scan_windows(target_ip)
    else:
        print("[-] Unsupported OS type. Use 'android' or 'windows'.")

if __name__ == "__main__":
    main()
