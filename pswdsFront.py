from tkinter import Tk, Label, Entry, Button, Listbox, messagebox as mb
from pswdsBend import PasswordKeeper


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
        self.password_entry = Entry(self.window, show="*")
        self.password_entry.pack()

        self.add_button = Button(self.window, text="Add Password", command=self.add_password)
        self.add_button.pack()

        self.password_list = Listbox(self.window, selectmode="single")
        self.password_list.pack()
        self.password_list.bind("<<ListboxSelect>>", self.show_password)

        self.refresh_password_list()

        self.window.mainloop()

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

    def show_password(self, event):
        selected_index = self.password_list.curselection()
        if selected_index:
            selected_password = self.password_list.get(selected_index)
            password_parts = selected_password.split(" | ")
            website = password_parts[0].split(": ")[1]
            username = password_parts[1].split(": ")[1]
            password_data = self.password_keeper.get_password(website)
            encrypted_password = password_data['password']
            decrypted_password = self.password_keeper.decrypt_password(encrypted_password)

            # Create a new window to display password details
            password_window = Tk()
            password_window.title("Password Details")

            website_label = Label(password_window, text="Website:")
            website_label.pack()
            website_value = Label(password_window, text=website)
            website_value.pack()

            username_label = Label(password_window, text="Username:")
            username_label.pack()
            username_value = Label(password_window, text=username)
            username_value.pack()

            password_label = Label(password_window, text="Password:")
            password_label.pack()

            # Entry widget to display the password (hidden initially)
            password_entry = Entry(password_window, show="*")
            password_entry.pack()

            def toggle_visibility():
                current_show_state = password_entry.cget("show")
                if current_show_state == "":
                    password_entry.config(show="*")
                    visibility_button.config(text="Show Password")
                else:
                    password_entry.config(show="")
                    visibility_button.config(text="Hide Password")

            # Button to toggle password visibility
            visibility_button = Button(password_window, text="Show Password", command=toggle_visibility)
            visibility_button.pack()

            # Set the password value in the entry widget
            password_entry.insert(0, decrypted_password)

            password_window.mainloop()
        else:
            mb.showwarning("No Selection", "Please select a password to view details.")


if __name__ == "__main__":
    password_keeper = PasswordKeeper("passwords.json")
    gui = PasswordKeeperGUI(password_keeper)
