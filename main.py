import sys
import json
import os
import subprocess
import tkinter as tk
from tkinter import messagebox


class Authentication:
    def __init__(self):
        self.credentials = {}
        self.load_credentials()

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
        self.credentials[username] = password
        self.save_credentials()

    def authenticate(self, username, password):
        return self.credentials.get(username) == password


class LoginWindow:
    def __init__(self, authentication):
        self.authentication = authentication

        self.root = tk.Tk()
        self.root.title("Login")

        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.authentication.authenticate(username, password):
            self.root.destroy()
            pass_trap_path = os.path.join(os.path.dirname(__file__), "Pass_Trap.py")
            python_path = sys.executable
            subprocess.call([python_path, pass_trap_path])
        else:
            messagebox.showerror("Error", "Invalid username or password.")


if __name__ == "__main__":
    authentication = Authentication()
    login_window = LoginWindow(authentication)
    login_window.root.mainloop()
