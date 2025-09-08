from collections import defaultdict
with open("log.txt", "r") as file:
    logs = file.readlines()

failed_attempts = defaultdict(int)

print("=== Suspicious Login Attempts ===")
for line in logs:
    if "LOGIN FAIL" in line:
        parts = line.strip().split(" - ")
        ip = parts[-1].split(": ")[1]
        failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"Possible brute-force attack from IP: {ip} ({count} failed attempts)")
