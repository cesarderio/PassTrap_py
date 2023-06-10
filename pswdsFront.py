from tkinter import Tk, Label, Entry, Button, Listbox, Checkbutton, BooleanVar, messagebox as mb, Frame
import random
import string
from tkinter import messagebox, simpledialog

from pswdsBend import PasswordKeeper


class PasswordKeeperGUI:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper
        self.window = Tk()
        self.window.title("Password Keeper")
        self.window.geometry("410x425")

        self.website_label = Label(self.window, text="Website:", anchor="center")
        self.website_label.pack()
        self.website_entry = Entry(self.window, width=30, justify="center")
        self.website_entry.pack()

        self.username_label = Label(self.window, text="Username:", anchor="center")
        self.username_label.pack()
        self.username_entry = Entry(self.window, width=30, justify="center")
        self.username_entry.pack()

        self.password_label = Label(self.window, text="Password:", anchor="center")
        self.password_label.pack()
        self.password_entry = Entry(self.window, width=30, show="*", justify="center")
        self.password_entry.pack()

        self.show_password_var = BooleanVar()
        self.show_password_checkbox = Checkbutton(self.window, text="Show Password", variable=self.show_password_var,
                                                  command=self.toggle_password_visibility)
        self.show_password_checkbox.pack()

        self.generate_button = Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.button_frame = Frame(self.window)
        self.button_frame.pack()

        self.add_button = Button(self.button_frame, text="Add", command=self.add_password)
        self.add_button.pack(side="left", padx=5, pady=5)

        self.update_button = Button(self.button_frame, text="Update", command=self.update_password)
        self.update_button.pack(side="left", padx=5, pady=5)

        self.delete_button = Button(self.button_frame, text="Delete", command=self.delete_password)
        self.delete_button.pack(side="left", padx=5, pady=5)

        self.password_list = Listbox(self.window, width=30, height=10, selectmode="single")
        self.password_list.pack()

        self.password_list.bind("<<ListboxSelect>>", self.show_password_entry)

        self.refresh_password_list()

        self.center_listbox_text()

        self.window.mainloop()

    def generate_password(self):
        password_length = 12
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
        self.password_entry.delete(0, 'end')
        self.password_entry.insert('end', generated_password)
        self.show_password_var.set(False)  # Hide the generated password by default

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

    def update_password(self):
        website = self.website_entry.get()
        new_password = self.password_entry.get()

        if website and new_password:
            if self.password_keeper.update_password(website, new_password):
                mb.showinfo("Success", "Password updated successfully.")
                self.clear_entry_fields()
                self.refresh_password_list()
            else:
                mb.showwarning("Error", "Website not found.")
        else:
            mb.showwarning("Error", "Please fill in both fields.")

    def delete_password(self):
        selected_index = self.password_list.curselection()
        if selected_index:
            selected_password = self.password_list.get(selected_index)
            password_parts = selected_password.split(" | ")
            website = password_parts[0].split(": ")[1]

            confirm = mb.askyesno("Confirmation", f"Are you sure you want to delete the password for '{website}'?")
            if confirm:
                if self.password_keeper.delete_password(website):
                    mb.showinfo("Success", "Password deleted successfully.")
                    self.clear_entry_fields()
                    self.refresh_password_list()
                else:
                    mb.showwarning("Error", "Website not found.")
        else:
            mb.showwarning("No Selection", "Please select a password to delete.")

    def clear_entry_fields(self):
        self.website_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def refresh_password_list(self):
        self.password_list.delete(0, 'end')
        passwords = self.password_keeper.get_passwords()

        for website, password_info in passwords.items():
            username = password_info['username']
            item_text = f"Website: {website} | Username: {username}"
            self.password_list.insert('end', item_text)

    def ask_pin(self):
        pin = simpledialog.askstring("PIN Required", "Enter the PIN to show the password:", show="*")
        return pin


    # def show_password_entry(self, event):
    def show_password_entry(self, event):
        selected_item = self.password_list.curselection()
        if selected_item:
            website_username = self.password_list.get(selected_item)
            website, username = self.extract_website_username(website_username)
            password_info = self.password_keeper.get_password_info(website)
            decrypted_password = password_info.get('password') if password_info else None
            pin = self.ask_pin()
            if pin is not None and self.password_keeper.check_pin(website, pin):
                self.clear_entry_fields()
                self.website_entry.delete(0, 'end')
                self.website_entry.insert('end', website)
                self.username_entry.delete(0, 'end')
                self.username_entry.insert('end', username)
                self.password_entry.delete(0, 'end')
                self.password_entry.insert('end', decrypted_password)
                self.show_password_var.set(False)  # Hide the password by default
            else:
                mb.showwarning("Invalid PIN", "Incorrect PIN. Please try again.")
        else:
            mb.showwarning("No Selection", "Please select a password entry.")

    def extract_website_username(self, website_username):
        website, username = website_username.split(" | ")
        website = website.split(": ")[1]
        username = username.split(": ")[1]
        return website, username




    def toggle_password_visibility(self):
        show_password = self.show_password_var.get()
        if show_password:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def center_listbox_text(self):
        # Set the listbox text alignment to center
        self.password_list.configure(justify='center')
        # Set the width of the listbox columns to center-align the text
        self.password_list.columnconfigure(0, weight=1)
        self.password_list.columnconfigure(1, weight=1)


if __name__ == "__main__":
    file_path = input("Enter the file name: ")
    pin = input("Enter the PIN: ")
    password_keeper = PasswordKeeper(file_path, pin)
    gui = PasswordKeeperGUI(password_keeper)
