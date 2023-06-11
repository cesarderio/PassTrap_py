from tkinter import messagebox, simpledialog
from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI

import os

def main():
    # file_path = input("Enter the file name: ")
    # pin = input("Enter the PIN: ")
    file_path = "PassTrap.txt"

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

    # password_keeper = PasswordKeeper(file_path, pin)
    password_keeper = PasswordKeeper(file_path, None)
    gui = PasswordKeeperGUI(password_keeper)


if __name__ == "__main__":
    main()
