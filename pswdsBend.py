import json
import os
from cryptography.fernet import Fernet


class PasswordKeeper:
    def __init__(self, file_path, pin):
        self.file_path = file_path
        self.pin = pin
        self.passwords = {}
        self.key = self.generate_key()

        self.load_passwords()

    def generate_key(self):
        key_file_path = self.file_path + ".key"
        if os.path.exists(key_file_path):
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)

        return key

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password.decode()

    def decrypt_password(self, encrypted_password):
        try:
            cipher_suite = Fernet(self.key)
            decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
            return decrypted_password.decode()
        except:
            return None

    def load_passwords(self):
        try:
            with open(self.file_path, "r") as file:
                data = file.read()
                if data.strip():
                    self.passwords = json.loads(data)
                else:
                    self.passwords = {}
        except FileNotFoundError:
            self.passwords = {}

    def save_passwords(self):
        with open(self.file_path, "w") as file:
            file.write(json.dumps(self.passwords))

    def add_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.passwords[website] = {"username": username, "password": encrypted_password}
        self.save_passwords()

    def update_password(self, website, new_password):
        if website in self.passwords:
            encrypted_password = self.encrypt_password(new_password)
            self.passwords[website]["password"] = encrypted_password
            self.save_passwords()
            return True
        return False

    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            self.save_passwords()
            return True
        return False

    def get_password_info(self, website):
        if website in self.passwords:
            password_info = self.passwords[website]
            decrypted_password = self.decrypt_password(password_info["password"])
            if decrypted_password is not None:
                return {"username": password_info["username"], "password": decrypted_password}
            else:
                print("Decryption failed for website:", website)  # Add this line
        else:
            print("Website not found in password records:", website)  # Add this line
        return None



    def check_pin(self, website, entered_pin):
        if website in self.passwords:
            return entered_pin == self.pin
        return False

    def get_passwords(self):
        return self.passwords
    
    def check_pin(self, website, pin):
        if self.pin:
            return pin == self.pin
        return True
