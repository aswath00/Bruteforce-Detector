# Bruteforce Detector

A Python script to detect **suspicious login attempts** from server logs. This tool helps identify potential brute-force attacks by counting failed login attempts per IP address.

## Features

- Reads server logs (`log.txt`) and analyzes failed login attempts.
- Flags IPs with **3 or more consecutive failed login attempts**.
- Lightweight and easy to use.
- Ideal for small-scale security monitoring and learning purposes.

## How it Works

- Reads each line of the log file.

- Looks for "LOGIN FAIL" entries.

- Extracts the IP address and counts failed attempts.

- Flags any IP with 3 or more failed attempts as suspicious.

## Demo

**Sample log file ('log.txt'):**

![Log File](/demo/log.png)

**Sample run of the script:**

![Script Output](/demo/op.png)

## Usage

1. Clone the repository:

```
git clone https://github.com/aswath00/Bruteforce-Detector.git
cd Bruteforce Detector'git commit
```
2. Run the script:

```
python analyze_logs.py
```
