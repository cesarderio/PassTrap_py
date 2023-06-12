import json
import os
from cryptography.fernet import Fernet


class PasswordKeeper:
    def __init__(self, file_path, pin=None):
        self.file_path = file_path
        self.pin = pin
        self.passwords = {}
        self.key = self.generate_key()

        self.load_passwords()
        
        self.credentials = {}  # Dictionary to store username-password pairs
        self.load_credentials()

        self.pin = self.get_pin()
        if self.pin is None:
            self.set_pin()

    def get_pin(self):
        try:
            with open("pin.txt", "r") as file:
                pin = file.read().strip()
            return pin if pin else None
        except FileNotFoundError:
            return None

    def set_pin(self):
        pin = input("Enter a new PIN: ")
        with open("pin.txt", "w") as file:
            file.write(pin)

        self.pin = pin


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

    def update_password(self, website, new_website, new_username, new_password):
        if website in self.passwords:
            password_info = self.passwords[website]
            del self.passwords[website]
            password_info['website'] = new_website
            password_info['username'] = new_username
            password_info['password'] = self.encrypt_password(new_password)
            self.passwords[new_website] = password_info
            self.save_passwords()
            return True
        else:
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
                print("Decryption failed for website:", website)
        else:
            print("Website not found in password records:", website)
        return None

    def check_pin(self, website, entered_pin):
        if website in self.passwords:
            # print("Stored Pin:", self.pin)  # Debugging statement
            # print("Entered Pin:", entered_pin)  # Debugging statement
            return entered_pin == self.pin
        return False


    def get_passwords(self):
        return self.passwords
    
    def load_credentials(self):
        try:
            with open("credentials.json", "r") as file:
                self.credentials = json.load(file)
        except FileNotFoundError:
            self.credentials = {}

    def save_credentials(self):
        with open("credentials.json", "w") as file:
            json.dump(self.credentials, file)

    def set_credentials(self, username, password):
        # Set up username and password
        self.credentials[username] = password
        self.save_credentials()

    def authenticate(self, username, password):
        # Authenticate the provided username and password
        # Check if the username exists in the credentials dictionary
        # If it does, compare the stored password with the provided password
        # Return True if the authentication is successful, False otherwise
        if username in self.credentials and self.credentials[username] == password:
            return True
        else:
            return False
