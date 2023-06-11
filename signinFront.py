from tkinter import Tk, Label, Entry, Button, messagebox


class SigninWindow:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper
        self.window = Tk()
        self.window.title("Sign In")

        self.username_label = Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        self.password_label = Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.window, show="*")
        self.password_entry.pack()

        self.setup_button = Button(self.window, text="Set up", command=self.setup)
        self.setup_button.pack()

        self.signin_button = Button(self.window, text="Sign In", command=self.signin)
        self.signin_button.pack()

        self.signed_in = False

        self.window.protocol("WM_DELETE_WINDOW", self.handle_close)  # Handle window close event
        self.window.withdraw()  # Hide the sign-in window initially

    def setup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.password_keeper.set_credentials(username, password)
            messagebox.showinfo("Setup Complete", "Username and password have been set.")
        else:
            messagebox.showerror("Setup Error", "Please enter both username and password.")

    def signin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.password_keeper.authenticate(username, password):
            self.signed_in = True
            self.window.destroy()
        else:
            messagebox.showerror("Sign In Failed", "Invalid username or password.")

    def is_signed_in(self):
        return self.signed_in

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()

    def handle_close(self):
        self.window.destroy()
