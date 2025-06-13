# merge.py

import requests
import sys

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
had_error = False

for url in urls:
    try:
        print(f"🔗 Fetching: {url}")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        for line in resp.text.splitlines():
            line = line.strip()
            if line and not line.startswith(('!', '#')):
                merged.add(line)
    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")
        had_error = True

if not merged:
    print("❌ No data fetched. Exiting with error.")
    sys.exit(1)

with open("merged.txt", "w", encoding="utf-8") as out:
    out.write("! Merged Adblock list – updated daily\n")
    for item in sorted(merged):
        out.write(item + "\n")

print(f"✅ Successfully wrote {len(merged)} entries to merged.txt")

# Nếu chỉ một vài lỗi, vẫn coi là thành công
sys.exit(0)
