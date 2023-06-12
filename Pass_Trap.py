from tkinter import messagebox, simpledialog
from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI

import os
import sys


def main():
    # Get the username from the command-line argument
    username = sys.argv[1] if len(sys.argv) > 1 else ""

    # Construct the database file path based on the username
    file_path = f"PassTrap_{username}.txt"

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

    password_keeper = PasswordKeeper(file_path)
    gui = PasswordKeeperGUI(password_keeper)


if __name__ == "__main__":
    main()

# Check if the shared file exists
shared_file_path = os.path.join(os.path.dirname(__file__), "shared.txt")
if os.path.exists(shared_file_path):
    # Close the shared file and remove it
    with open(shared_file_path, "r") as file:
        content = file.read().strip()
    os.remove(shared_file_path)

    # Check if the content indicates to close the login window
    if content == "close_login_window":
        messagebox.showinfo("Success", "Authentication successful!")
        sys.exit(0)
