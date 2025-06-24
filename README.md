
---

### 4. File Integrity Monitor

```markdown
# 🗂️ File Integrity Monitor

> Detects changes to specified files by monitoring file hashes periodically.

## Description

Monitors a target file for any modifications by hashing its contents at regular intervals. Alerts on any detected changes. Useful for basic tampering detection.

## Features

- Computes SHA-256 hash of target file  
- Periodically checks for changes  
- Prints alerts on modification

## Requirements

No external dependencies; uses standard Python libraries.

## Usage

Edit the `WATCH_FILE` variable in the script to target your file.

Run the script:

```bash
python file_integrity_monitor.py
