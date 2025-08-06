

https://github.com/user-attachments/assets/f7983ad0-102e-4c04-a9e0-f71462a4f890

<h1 align="center">
  🕷️ BUGSCAN-MR 🕷️<br>
  <sub><i>By MrPYTHON • SecretNet Crew ☠️</i></sub>
</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/MrPYTHONI/bugscan-mr/main/banner.png" alt="BUGSCAN-MR BANNER" />
</p>

---

> ⚠️ WARNING: This tool is not for the faint of heart.  
> 🧠 Created by real hackers, for real recon.

---

## 💀 About `bugscan-mr`

`bugscan-mr` is a multi-purpose, ultra-aggressive recon & CDN hunting tool designed to rip apart domains, IP ranges, and even APK files to find hidden endpoints, vulnerable assets, and secrets in the shadows.

It’s built with power, speed, and style—wrapped in a terrifying terminal experience ☠️

---

## ⚙️ Features

🧠 **Massive Domain Scanner**  
- Scan domains via `SNI`, `SSL`, `HTTP`, `HTTPS`, and `Proxy`  
- Multithreaded. Fast. Brutal.

🧠 **Subdomain Extraction (Smart Recon Mode)**  
- From file or single domain  
- Combines multiple sources:  
  - `subfinder`  
  - `crt.sh`  
  - `alienvault`  
  - `dnsdumpster`  
  - (optional) VirusTotal API  
- Saves beautiful subdomain lists

🧠 **CIDR CDN Scanner**  
- Scan CIDR IP ranges for CDN fingerprints  
- Detects servers like `cloudflare`, `google frontend`, `akamai`, and more  
- Automatically filters noise like 302 redirects

🧠 **DNS Range Scanner**  
- Fast UDP DNS probing  
- Useful for discovering internal or exposed DNS servers in large IP blocks

🧠 **APK CDN Hunter**  
- Extract URLs, domains, and CDN references from `.apk` files  
- Highlight hidden payment links, CDN servers, and sensitive endpoints  
- Useful for analyzing Android app infrastructure

🧠 **IP Resolver**  
- Convert list of domains to IP addresses  
- Fast multithreaded resolution with beautiful output

---

## 🧪 Installation

```bash
git clone https://github.com/MrPYTHONI/bugscan-mr.git
cd bugscan-mr
python3 install.py
```



🕹️ Usage

python3 bugscan.py 

Interactive CLI will guide you through scanning, subdomain hunting, CIDR attacks, and more...

🧠 Screenshots

￼ 

👁️ Credits

🧠 Developed by: MrPYTHON ☠

🔗 Telegram: https://t.me/SECRET1NET

🎥 YouTube: https://youtube.com/@mr_python3?si=5HfhUxJOHlRCf1EA

📜 More tools: https://mrpython3.carrd.co/ 

⚠️ Legal Disclaimer

This tool is made for educational and authorized testing purposes only.
The creator takes no responsibility for any misuse. Use responsibly.

🧠 bugscan-mr — when normal recon isn’t enough... unleash the hacker within 🕷️

