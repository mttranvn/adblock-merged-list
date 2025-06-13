import requests

urls = [
    "https://github.com/bigdargon/hostsVN/raw/master/hosts",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.plus.mini.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.amazon.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.apple.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.huawei.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.winoffice.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.samsung.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.tiktok.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.tiktok.extended.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.roku.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/native.xiaomi.txt",
    "https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardDNS.txt"
]

merged = set()

for url in urls:
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        for line in resp.text.splitlines():
            line = line.strip()
            if line and not line.startswith(('!', '#')):
                merged.add(line)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

with open("merged.txt", "w", encoding="utf-8") as out:
    out.write("! Merged Adblock list – updated daily\n")
    for item in sorted(merged):
        out.write(item + "\n")
