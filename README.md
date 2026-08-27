# File Integrity Checker

A Python tool that detects unauthorized file changes using SHA-256 hashing — 
a simplified version of what tools like Tripwire and OSSEC use in production 
environments to monitor critical system files.

## How It Works

1. **Baseline creation** — calculates the SHA-256 hash of a file and saves it 
   as a "fingerprint" in `baseline.json`
2. **Integrity check** — recalculates the file's current hash and compares it 
   against the saved baseline
3. If even a single byte has changed, the hashes won't match — flagging the 
   file as modified

## Features

- SHA-256 hashing (cryptographically secure, collision-resistant)
- Supports checking multiple files at once
- Detects three states: unchanged, modified, or missing
- Persists baseline data in JSON, so checks can be run anytime after setup
- Reads files in chunks — handles large files without high memory usage

## Usage

```bash
python file_integrity_checker.py
```

Menu options:
- **1. Add file(s) to baseline** — hash a file and save it as the trusted reference
- **2. Check integrity against baseline** — compare current files against saved hashes
Choose an option (1-3): 1
Enter file path(s), separated by commas: important.txt
[ADDED] important.txt
Baseline saved to baseline.json

Choose an option (1-3): 2
Checking 1 file(s) against baseline...
[OK] important.txt — unchanged


After modifying the file:

Choose an option (1-3): 2
Checking 1 file(s) against baseline...
[MODIFIED] important.txt — hash mismatch! File has changed.


## Why This Matters

File integrity monitoring is a core defensive security technique used to detect:
- Malware modifying system files
- Unauthorized configuration changes
- Tampering with logs or critical data

Hashing is preferred over checking file size or timestamps because those can 
be spoofed — a cryptographic hash changes completely even if a single 
character in the file is altered.

## What I Learned

- Cryptographic hashing (SHA-256) with Python's `hashlib`
- Reading files safely in chunks for memory efficiency
- Persisting state between runs using JSON
- Practical use case for a core blue-team / defensive security concept

## Tech Stack
- Python 3
- hashlib(SHA-256)
- json (baseline storage)
