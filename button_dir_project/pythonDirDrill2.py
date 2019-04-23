from tkinter import *
import tkinter as tk
from tkinter import constants, filedialog
import os
import shutil 
import sqlite3

import pythonDbDrill
import pythonDrill_1


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(1000,1000)
        self.master.title("User Info Page")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master
        destination_button()
        



curr_directory = os.getcwd()


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def destination_button():
    global folder_path
    txtFileName = filedialog.askopenfilename(initialdir = curr_directory, title = "Select file", filetypes = (("text files", "*.txt"), ("all files","*.*")))
    folder_path.set(txtFileName)
    print(txtFileName)

conn = sqlite3.connect('move.db')


shutil.move('academy.db', 'move.db')

conn = sqlite3.connect('move.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file2, col_file5 FROM tbl_fileList")
    conn.commit()
    varText = cur.fetchall()
    for text in varText:
        msg = "File Name1: {}\nFile Name2: {}".format(text[0], text[1])
    print(msg)
conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    folder_path = StringVar()
    lbl1 = Label(master=root,textvariable=folder_path)
    lbl1.grid(row=0, column=1)
    button2 = Button(text="Choose your text file please", command=destination_button)
    button2.grid(row=0, column=3)
    button3 = Button(text="Choose your path please", command=browse_button)
    button3.grid(row=0, column=5)
    App = ParentWindow(root)
    root.mainloop()
