import sys
sys.stdout.reconfigure(line_buffering=True)

import hashlib

def create_hash(password):
    # Creating MD5 hash of password
    return hashlib.md5(password.encode()).hexdigest()

password = "aswath"
hashed_password = create_hash(password)
print(f"MD5 Hash for '{password}': {hashed_password}")