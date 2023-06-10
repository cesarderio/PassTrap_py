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


class PasswordKeeperGUI:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper
        self.root = tk.Tk()
        self.root.title("Password Keeper")
        self.password_list = tk.Listbox(self.root, width=50)
        self.password_list.pack(pady=20)
        self.password_list.bind('<<ListboxSelect>>', self.on_password_select)
        self.expand_button = tk.Button(self.root, text="Expand", command=self.toggle_password_visibility)
        self.expand_button.pack(pady=10)
        self.root.mainloop()

    def refresh_password_list(self):
        self.password_list.delete(0, tk.END)
        passwords = self.password_keeper.get_passwords()
        for website, data in passwords.items():
            self.password_list.insert(tk.END, website)

    def on_password_select(self, event):
        selection = self.password_list.curselection()
        if selection:
            index = selection[0]
            website = self.password_list.get(index)
            password_data = self.password_keeper.get_password(website)
            if password_data:
                username = password_data.get('username', '')
                password = password_data.get('password', '')
                messagebox.showinfo(website, f"Username: {username}\nPassword: {'*' * len(password)}")
            else:
                messagebox.showwarning("No Data", "No username and password data available.")

    def toggle_password_visibility(self):
        selection = self.password_list.curselection()
        if selection:
            index = selection[0]
            website = self.password_list.get(index)
            password_data = self.password_keeper.get_password(website)
            if password_data:
                username = password_data.get('username', '')
                password = password_data.get('password', '')
                messagebox.showinfo(website, f"Username: {username}\nPassword: {password}")
            else:
                messagebox.showwarning("No Data", "No username and password data available.")


file_path = input("Enter the file name: ")
password_keeper = PasswordKeeper(file_path)
gui = PasswordKeeperGUI(password_keeper)
