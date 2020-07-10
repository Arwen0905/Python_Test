# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:24:06 2020

@author: ASUS
"""

from tkinter import messagebox
import tkinter
# import tkMessageBox

top = tkinter.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()