from pswdsBend import PasswordKeeper
from pswdsFront import PasswordKeeperGUI

file_path = input("Enter the file name: ")
password_keeper = PasswordKeeper(file_path)
gui = PasswordKeeperGUI(password_keeper)
gui.window.mainloop()
