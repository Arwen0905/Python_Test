# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:50:59 2020

@author: ASUS
"""


from tkinter import *  
  
top = Tk()  
  
def hello():  
    print("hello!")  

def tkquit():
    top.destroy()
# create a toplevel menu  
menubar = Menu(top)  
menubar.add_command(label="Hello!", command=hello)  
menubar.add_command(label="Quit!", command=tkquit)  
  
# display the menu  
top.config(menu=menubar)  
  
top.mainloop()  