import os
from cryptography.fernet import Fernet

if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)