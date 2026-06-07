from cryptography.fernet import Fernet
import os

def get_cipher():
    with open("key.key", "rb") as f:
        key = f.read()
        return Fernet(key)

def encrypt_password(password):
    return get_cipher().encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    try:
        return get_cipher().decrypt(encrypted_password.encode()).decode()
    except Exception:
        return None