import subprocess

def check_nmap_installed():
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("[-] Nmap is not installed. Install it with:\n  sudo apt install nmap")
        exit(1)

def get_os_type():
    os_type = input("Target OS (android/windows): ").strip().lower()
    if os_type not in ["android", "windows"]:
        print("[-] Invalid OS type. Choose 'android' or 'windows'.")
        exit(1)
    return os_type

def get_target_ip():
    return input("Enter target IP address: ").strip()

def scan(ip, os_type):
    print(f"[+] Starting scan on {ip} (Target OS: {os_type})...")
    
    if os_type == "android":
        ports = "5555,8080,12345"
    else:
        ports = "21,22,80,139,445,3389"

    cmd = ["nmap", "-sS", "-T4", "-p", ports, ip]
    subprocess.run(cmd)

def main():
    check_nmap_installed()
    os_type = get_os_type()
    ip = get_target_ip()
    scan(ip, os_type)

if __name__ == "__main__":
    main()
