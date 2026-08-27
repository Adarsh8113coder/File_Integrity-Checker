#!/usr/bin/env python3
"""
File Integrity Checker
------------------------
Calculates SHA-256 hashes of files and detects if they've been modified
by comparing against a saved baseline. This is how tools detect tampering
or unauthorized changes to important files (e.g., system files, configs).

Usage:
    python file_integrity_checker.py
"""

import hashlib
import json
import os
BASELINE_FILE = "baseline.json"
def calculate_hash(filepath):
    """Calculate the SHA-256 hash of a file's contents."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None


def load_baseline():
    """Load previously saved hashes, if they exist."""
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_baseline(baseline):
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=2
def add_files_to_baseline(filepaths):
    baseline = load_baseline()
    for path in filepaths:
        file_hash = calculate_hash(path)
        if file_hash is None:
            print(f"  [SKIPPED] {path} — file not found")
            continue
        baseline[path] = file_hash
        print(f"  [ADDED] {path}")
    save_baseline(baseline)
    print(f"\nBaseline saved to {BASELINE_FILE}")


def check_integrity():
    baseline = load_baseline()
    if not baseline:
        print("No baseline found. Add files to a baseline first (option 1).")
        return

    print(f"\nChecking {len(baseline)} file(s) against baseline...\n")

    for path, old_hash in baseline.items():
        current_hash = calculate_hash(path)

        if current_hash is None:
            print(f"  [MISSING] {path} — file no longer exists!")
        elif current_hash == old_hash:
            print(f"  [OK]      {path} — unchanged")
        else:
            print(f"  [MODIFIED] {path} — hash mismatch! File has changed.")


def main():
    print("=" * 55)
    print("FILE INTEGRITY CHECKER")
    print("=" * 55)

    while True:
        print("\nOptions:")
        print("  1. Add file(s) to baseline")
        print("  2. Check integrity against baseline")
        print("  3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            paths_input = input("Enter file path(s), separated by commas: ")
            filepaths = [p.strip() for p in paths_input.split(",")]
            add_files_to_baseline(filepaths)

        elif choice == "2":
            check_integrity()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
