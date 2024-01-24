import tkinter as tk
from tkinter import Label, Button


class AboutTorPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg="black")

        # Text data for the Dark Web Wikipedia page
        dark_web_info = """
        The dark web is the World Wide Web content that exists on 
        darknets, overlay networks that use the Internet but require 
        specific software, configurations, or authorization to access. 
        The dark web forms a small part of the deep web, the part of 
        the Web not indexed by web search engines, although sometimes 
        the term deep web is mistakenly used to refer specifically to 
        the dark web.

        The darknets that constitute the dark web include small, 
        friend-to-friend peer-to-peer networks, as well as large, 
        popular networks such as Tor, Freenet, I2P, and Riffle 
        operated by public organizations and individuals. Users of 
        the dark web refer to the regular web as the Clearnet due 
        to its unencrypted nature. The Tor dark web may be referred 
        to as onionland, a reference to the network's top-level domain 
        suffix .onion and the traffic anonymization technique of 
        onion routing.

        The dark web is often associated with illegal activities, 
        such as illegal trade, forums, and media exchange for 
        criminals and terrorists. Many whistle-blowers use the dark 
        web to leak information or documents while keeping their 
        identities hidden.

        Source: https://en.wikipedia.org/wiki/Dark_web
        """

        # Display the text in a Label or Text widget, depending on your needs
        label_info = Label(self, text=dark_web_info, font=("Helvetica", 12), fg="white", bg="black", wraplength=600, justify="left")
        label_info.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # Home Button
        home_button = Button(self, text="Home", font=("Helvetica", 14), bg='#6699CC', fg='black',
                             activebackground='#336699', width=15, height=2,
                             command=lambda: self.controller.show_frame(HomePage))
        home_button.grid(row=1, column=0, pady=20, padx=20, sticky="w")

        # Exit Button
        exit_button = Button(self, text="Exit", font=("Helvetica", 14), bg='#CC6666', fg='black',
                             activebackground='#993333', width=15, height=2, command=parent.quit)
        exit_button.grid(row=1, column=1, pady=20, padx=20, sticky="e")
