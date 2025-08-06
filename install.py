#MrPYTHON
import os
import subprocess
import sys
import shutil

# Required Python packages
required_packages = [
    "beautifulsoup4",
    "requests",
    "rich",
    "colorama",
    "ipcalc"
]

# Install any missing packages using pip
def install_missing_packages():
    for package in required_packages:
        try:
            __import__(package if package != "beautifulsoup4" else "bs4")
        except ImportError:
            print(f"[+] Installing: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"[✓] {package} is already installed")

# Check if subfinder tool is installed
def check_subfinder():
    subfinder_path = shutil.which("subfinder")
    if subfinder_path:
        print(f"[✓] subfinder is installed: {subfinder_path}")
    else:
        print("[✗] subfinder is NOT installed!")
        print("👉 To install subfinder on Termux or Linux, run:")
        print("   pkg install golang")
        print("   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
        print("➡️ Then add $HOME/go/bin to your $PATH")

# Run the setup check
if __name__ == "__main__":
    print("🔧 Checking required Python libraries and subfinder...")
    install_missing_packages()
    check_subfinder()
