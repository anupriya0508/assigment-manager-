import tkinter as tk
from tkinter import messagebox
from database import get_user_by_username

class UserManager(tk.Frame):
    def __init__(self, parent, show_assignment_manager):
        super().__init__(parent)
        self.show_assignment_manager = show_assignment_manager
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="User Login")
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform user authentication (you need to implement this logic)
        user = get_user_by_username(username)

        # if user is not None and user["password"] == password:
        self.show_assignment_manager()
       # else:
        #    messagebox.showerror("Login Failed", "Invalid username or password.")

# You can expand this module to include user registration functionality as well.
