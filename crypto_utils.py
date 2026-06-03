from cryptography.fernet import Fernet

with open("key.key", "rb") as file:
    KEY = file.read()

cipher = Fernet(KEY)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(
        encrypted_password.encode()
    ).decode()