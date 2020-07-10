# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:56:32 2020

@author: ASUS
"""

# import tkinter
# # import tkMessageBox

# top = tkinter.Tk()


# !/usr/bin/python3
from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()


text1 = Text(root)
text1.insert(INSERT, "Hello2.....")
text1.insert(END, "Bye Bye2.....")
text1.pack()





text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")


text1.tag_add("here2", "1.1", "1.5")
text1.tag_add("start2", "1.8", "1.13")
text1.tag_config("here2", background = "yellow", foreground = "blue")
text1.tag_config("start2", background = "black", foreground = "green")

root.mainloop()