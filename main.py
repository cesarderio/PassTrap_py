import sys
import json
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI


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

    def reset_credentials(self):
        self.credentials = {}
        self.save_credentials()

    def authenticate(self, username, password):
        return self.credentials.get(username) == password


class LoginWindow:
    def __init__(self, authentication):
        self.authentication = authentication

        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("240x200")  # Set the window size (width x height)

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

        self.button_setup = tk.Button(self.root, text="Setup", command=self.setup)
        self.button_setup.pack()

        self.button_reset = tk.Button(self.root, text="Reset", command=self.reset)
        self.button_reset.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.authentication.authenticate(username, password):
            self.root.destroy()  # Close the login window

            file_path = "PassTrap_{}.txt".format(username)
            password_keeper = PasswordKeeper(file_path)
            gui = PasswordKeeperGUI(password_keeper)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def setup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password:
            self.authentication.set_credentials(username, password)
            messagebox.showinfo("Success", "Username and password have been set.")
        else:
            messagebox.showerror("Error", "Please enter a username and password.")

    def reset(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to reset credentials?")
        if confirm:
            self.authentication.reset_credentials()
            messagebox.showinfo("Success", "Credentials have been reset.")
        else:
            messagebox.showinfo("Cancelled", "Credentials reset has been cancelled.")


if __name__ == "__main__":
    authentication = Authentication()
    login_window = LoginWindow(authentication)
    login_window.root.mainloop()
