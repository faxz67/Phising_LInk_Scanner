import re
import requests
import tldextract
from colorama import Fore, Style

def is_suspicious_url(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    # Simple heuristics
    if re.search(r"@|%|#", url):
        return True, "Contains suspicious characters (@, %, #)"
    if url.count('-') > 3:
        return True, "Too many hyphens"
    if len(url) > 75:
        return True, "URL too long"
    if re.search(r"https?://\d{1,3}(\.\d{1,3}){3}", url):
        return True, "Uses IP address instead of domain"

    # WHOIS check or ML model can go here

    return False, "Seems normal"

def check_url(url):
    print(f"\nChecking: {url}")
    try:
        response = requests.head(url, timeout=5)
        status = response.status_code
        print(f"Status Code: {status}")
    except:
        print(f"{Fore.YELLOW}Warning: URL unreachable{Style.RESET_ALL}")
        return

    is_suspicious, reason = is_suspicious_url(url)
    if is_suspicious:
        print(f"{Fore.RED}[PHISHING DETECTED] {reason}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[SAFE] {reason}{Style.RESET_ALL}")

if __name__ == "__main__":
    url = input("Enter URL to check: ")
    check_url(url)
