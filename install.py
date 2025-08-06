# By MrPYTHON ☠️ - SecretNet Crew
import os
import subprocess
import sys
import shutil

# ✅ Required Python packages
required_packages = [
    "beautifulsoup4",
    "requests",
    "rich",
    "colorama",
    "ipcalc"
]

# ✅ Install missing Python packages
def install_missing_packages():
    for package in required_packages:
        try:
            __import__(package if package != "beautifulsoup4" else "bs4")
            print(f"[✓] {package} is already installed")
        except ImportError:
            print(f"[+] Installing: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# ✅ Install subfinder automatically if not found
def install_subfinder():
    print("[+] Installing Go and subfinder...")
    subprocess.call("pkg install -y golang", shell=True)
    subprocess.call("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest", shell=True)

    # Expected install path
    subfinder_bin = os.path.expanduser("~/go/bin/subfinder")
    if os.path.isfile(subfinder_bin):
        print(f"[✓] subfinder installed at: {subfinder_bin}")
        print("[*] Adding subfinder to PATH (temporary)...")
        os.environ["PATH"] += os.pathsep + os.path.expanduser("~/go/bin")
        print("[✓] Done! To make it permanent, run:")
        print('echo \'export PATH="$PATH:$HOME/go/bin"\' >> ~/.bash_profile && source ~/.bash_profile')
    else:
        print("❌ subfinder installation failed. Make sure Go is working properly.")

# ✅ Check if subfinder exists, install if not
def check_and_install_subfinder():
    if shutil.which("subfinder"):
        print("[✓] subfinder is already installed.")
    else:
        install_subfinder()

# ✅ Main execution
if __name__ == "__main__":
    print("🔧 Checking environment and installing requirements...")
    install_missing_packages()
    check_and_install_subfinder()
