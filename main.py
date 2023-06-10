from tkinter import messagebox, simpledialog
from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI


def main():
    file_path = input("Enter the file name: ")
    # pin = input("Enter the PIN: ")

    # password_keeper = PasswordKeeper(file_path, pin)
    password_keeper = PasswordKeeper(file_path, None)
    gui = PasswordKeeperGUI(password_keeper)


if __name__ == "__main__":
    main()
