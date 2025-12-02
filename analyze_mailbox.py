import os
import mailbox
import glob

BLOCKLIST = ["paypal.example.com", "malicious.example.com", "another.bad"]

def is_phishing(msg):
    body = msg.get_payload()
    for bad in BLOCKLIST:
        if bad in body:
            return True
    return False

def analyze():
    files = glob.glob("mailbox/*.eml")
    for f in files:
        with open(f, "r", errors="ignore") as raw:
            content = raw.read()

            if any(bad in content for bad in BLOCKLIST):
                print(f"[BLOCKED] {f}")
            else:
                print(f"[OK]      {f}")

if __name__ == "__main__":
    analyze()
