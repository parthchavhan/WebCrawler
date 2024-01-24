import tkinter as tk
from tkinter import Label, Entry, W, Button, Listbox

from crawl import search
from widgets import EntryWithPlaceholder

import csv
import time


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg='black')


        search_entry = EntryWithPlaceholder(self, "Enter Website to Crawl")
        search_button = Button(self, text="Search", font=("Helvetica", 14), bg='#6699CC', fg='black', command=lambda: self.crawl_url(search_entry.get()))

        drugs_button = Button(self, text='Drugs', font=("Helvetica", 14), bg='#6699CC', fg='black', command=lambda: self.search('Drugs'))
        weapons_button = Button(self, text='Weapons', font=("Helvetica", 14), bg='#6699CC', fg='black', command=lambda: self.search('Weapons'))

        self.result_listbox = Listbox(self, width=60, height=30)

        home_button = Button(self, text="Home", font=("Helvetica", 14), bg='#6699CC', fg='black',
                             activebackground='#336699', command=lambda: self.controller.show_frame(HomePage))
        exit_button = Button(self, text="Exit", font=("Helvetica", 14), bg='#CC6666', fg='red',
                             activebackground='#993333', command=parent.quit)
        exit_button.grid(row=2, column=6, pady=20)

        # grid widgets
        search_entry.grid(row=1, column=0, pady=(20, 10), padx=10)
        search_button.grid(row=1, column=1, pady=(20, 10), padx=10)

        drugs_button.grid(row=2, column=0, padx=10, pady=10)
        weapons_button.grid(row=2, column=1, padx=10, pady=10)

        self.result_listbox.grid(row=3, column=0, columnspan=2, padx=10)

        home_button.grid(row=0, column=0, pady=(10, 20), sticky=W, padx=10)

    def search(self, term):
        def get_data():
            with open('links.csv', "r") as csvfile:
                spamreader = csv.reader(csvfile)
                return [row for row in spamreader if row[1] == term]

        self.result_listbox.delete(0, tk.END)
        for i, a in enumerate(get_data()):
            self.result_listbox.insert(i, a)
            self.result_listbox.update()
            time.sleep(1)

    def crawl_url(self, url):
        self.result_listbox.delete(0, tk.END)
        for i, a in enumerate(search(url)):
            self.result_listbox.insert(i, a)
            self.result_listbox.update()
            time.sleep(1)