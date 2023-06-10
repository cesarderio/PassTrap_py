from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI

file_name = input("Enter the file name: ")
file_path = f"./{file_name}"

try:
    password_keeper = PasswordKeeper(file_path)
    gui = PasswordKeeperGUI(password_keeper)
    gui.run()
except FileNotFoundError as e:
    create_file = input("The file does not exist. Do you want to create it? (y/n): ")
    if create_file.lower() == "y":
        password_keeper = PasswordKeeper(file_path)
        gui = PasswordKeeperGUI(password_keeper)
        gui.run()
    else:
        print(e)
