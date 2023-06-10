from tkinter import Tk, Label, Entry, Button, Listbox, messagebox as mb
from pswdsBend import PasswordKeeper
import tkinter as tk
from tkinter import messagebox


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


class PasswordKeeperGUI:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper
        self.window = Tk()
        self.window.title("Password Keeper")
        self.window.geometry("400x500")

        self.website_label = Label(self.window, text="Website:")
        self.website_label.pack()
        self.website_entry = Entry(self.window)
        self.website_entry.pack()

        self.username_label = Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        self.password_label = Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.window)
        self.password_entry.pack()

        self.add_button = Button(self.window, text="Add Password", command=self.add_password)
        self.add_button.pack()

        self.password_list = Listbox(self.window, selectmode="single")
        self.password_list.pack()
        self.password_list.bind("<<ListboxSelect>>", self.expand_password)

        self.refresh_password_list()

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            self.password_keeper.add_password(website, username, password)
            self.clear_entry_fields()
            self.refresh_password_list()
        else:
            mb.showwarning("Error", "Please fill in all fields.")

    def clear_entry_fields(self):
        self.website_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def refresh_password_list(self):
      self.password_list.delete(0, 'end')
      passwords = self.password_keeper.get_passwords()

      for website, password_info in passwords.items():
          username = password_info['username']
          password = "*" * len(password_info['password'])  # Hide password initially
          item_text = f"Website: {website} | Username: {username} | Password: {password}"
          self.password_list.insert('end', item_text)

      self.password_list.bind('<<ListboxSelect>>', self.show_password)  # Bind the event to show password



    def expand_password(self, event):
        selected_index = self.password_list.curselection()
        selected_password = self.password_list.get(selected_index)
        password_parts = selected_password.split(" | ")
        website = password_parts[0].split(": ")[1]
        username = password_parts[1].split(": ")[1]
        password = password_parts[2].split(": ")[1]

        mb.showinfo("Expanded Password", f"Website: {website}\nUsername: {username}\nPassword: {password}")


    def show_password(self, event):
        selected_index = self.password_list.curselection()
        selected_password = self.password_list.get(selected_index)
        password_parts = selected_password.split(" | ")
        website = password_parts[0].split(": ")[1]
        username = password_parts[1].split(": ")[1]
        password = self.password_keeper.get_password(website)['password']  # Retrieve the decrypted password
        decrypted_password = self.password_keeper.decrypt_password(password)
        password_text = f"Website: {website} | Username: {username} | Password: {decrypted_password}"

        # Update the password item with the decrypted password
        self.password_list.delete(selected_index)
        self.password_list.insert(selected_index, password_text)
        self.password_list.itemconfig(selected_index, fg='blue')



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    file_path = input("Enter the file name: ")
    password_keeper = PasswordKeeper(file_path)
    gui = PasswordKeeperGUI(password_keeper)
    gui.run()
