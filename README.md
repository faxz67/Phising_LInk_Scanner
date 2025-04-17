# 🛡️ Phishing Link Scanner

A simple Python-based tool to detect potentially **malicious or phishing URLs** using rule-based heuristics and basic URL analysis. This project is ideal for cybersecurity students, interns, and beginners who want to learn how phishing detection works.

---

## 📌 Features

- ✅ Detects suspicious characters like `@`, `%`, `#`
- ✅ Flags IP-based domains instead of real domains
- ✅ Warns about too many hyphens or unusually long URLs
- ✅ Checks HTTP response status of a link
- ✅ Color-coded output for clear results
- ✅ Lightweight and beginner-friendly

---

## 🎯 How It Works

The scanner evaluates a URL based on:
- Structure of the domain
- Presence of suspicious symbols
- Length of the URL
- Use of raw IP addresses
- Basic server response (using `requests.head()`)

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/phishing-link-scanner.git
cd phishing-link-scanner
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
