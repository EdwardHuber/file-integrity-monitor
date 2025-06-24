import hashlib
import os
import time

WATCH_FILE = "important.txt"
CHECK_INTERVAL = 5  # seconds

def hash_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor_file(filepath):
    last_hash = hash_file(filepath)
    print(f"Monitoring {filepath}...")

    while True:
        time.sleep(CHECK_INTERVAL)
        current_hash = hash_file(filepath)
        if current_hash != last_hash:
            print("[!] File change detected!")
            last_hash = current_hash
        else:
            print("[✓] No change.")

monitor_file(WATCH_FILE)
