import tkinter as tk
from tkinter import Label, Button
from PIL import ImageTk, Image
from search import SearchPage
from about_tor import AboutTorPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")

        # Logo
        image = Image.open("images/download.png")
        image = image.resize((200, 200), Image.LANCZOS)
        logo = ImageTk.PhotoImage(image)
        label = Label(self, image=logo, bg="#F5F5F5")
        label.image = logo
        label.grid(row=0, column=0, pady=20, padx=20, sticky='n')

        # Header
        header_label = Label(self, text="Services we Provide!!", font=("Helvetica", 20), bg="black", fg="white")
        header_label.grid(row=1, column=0, pady=(0, 20))

        # Buttons
        buttons_frame = tk.Frame(self, bg="black")
        buttons_frame.grid(row=2, column=0, pady=(0, 20), padx=20)

        search_button = Button(buttons_frame, text="Search Terms", font=("Helvetica", 16),
                               bg="#6699CC", fg="black", activebackground="#336699", width=20, height=2,
                               command=lambda: controller.show_frame(SearchPage))
        search_button.pack(side='left', padx=(0, 10))

        about_tor_button = Button(buttons_frame, text="About Tor", font=("Helvetica", 16),
                                  bg="#6699CC", fg="black", activebackground="#336699", width=20, height=2,
                                  command=lambda: controller.show_frame(AboutTorPage))
        about_tor_button.pack(side='left', padx=(0, 10))

        exit_button = Button(self, text="EXIT", font=("Helvetica", 16), bg="#CC6666", fg="red",
                             activebackground="#993333", width=20, height=2,
                             command=parent.quit)
        exit_button.grid(row=3, column=0, pady=(0, 10), padx=20, sticky='s')
