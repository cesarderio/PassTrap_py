import tkinter as tk
from tkinter import messagebox
import json
from cryptography.fernet import Fernet, InvalidToken


class PasswordKeeper:
    def __init__(self, file_path):
        self.file_path = file_path
        self.key = self.load_key()
        self.passwords = {}
        self.load_passwords_from_file()

    def load_key(self):
        try:
            with open("key.key", "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
        return key

    def load_passwords_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                data = file.read()
                if data:
                    decrypted_data = self.decrypt_data(data)
                    try:
                        self.passwords = json.loads(decrypted_data)
                    except json.JSONDecodeError:
                        self.passwords = {}
                else:
                    self.passwords = {}
        except FileNotFoundError:
            self.passwords = {}

    def save_passwords_to_file(self):
        with open(self.file_path, "w") as file:
            encrypted_data = self.encrypt_data(json.dumps(self.passwords))
            file.write(encrypted_data)

    def add_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.passwords[website] = {
            'username': username,
            'password': encrypted_password.decode()
        }
        self.save_passwords_to_file()

    def get_passwords(self):
        return self.passwords
    
    def get_password(self, website):
        return self.passwords.get(website, {})

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
        return decrypted_password.decode()

    def encrypt_data(self, data):
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        try:
            decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except InvalidToken:
            return ""
