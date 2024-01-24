
from home import HomePage



import tkinter as tk
from tkinter import Label, Entry, W, Button


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg="black")

        l1 = Label(self, text="Hello Team Spider", bg="black", fg="white", font=("Arial", 16))
        l1.place(relx=0.5, rely=0.3, anchor="center")

        Label(self, text="Username:", font=("Arial", 12), bg="black", fg="white").place(relx=0.4, rely=0.45, anchor="center")
        username_entry = Entry(self, font=("Arial", 12), bg="white")
        username_entry.place(relx=0.6, rely=0.45, anchor="center")

        Label(self, text="Password:", font=("Arial", 12), bg="black", fg="white").place(relx=0.4, rely=0.55, anchor="center")
        password_entry = Entry(self, font=("Arial", 12), bg="white", show="*")
        password_entry.place(relx=0.6, rely=0.55, anchor="center")

        button = Button(self, text="Log In", font=("Arial", 12), bg="white", fg='black', command=lambda: self.click_login(username_entry.get(), password_entry.get()))
        button.place(relx=0.5, rely=0.7, anchor="center")

        exit_button = Button(self, text="Exit", font=("Arial", 12), bg="white",  fg='red', command=parent.quit)
        exit_button.place(relx=0.9, rely=0.9, anchor="center")

    def click_login(self, username, password):

            self.controller.show_frame(HomePage)

