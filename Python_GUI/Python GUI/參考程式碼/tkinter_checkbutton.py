# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:23:06 2020

@author: ASUS
"""


from tkinter import *   


def selection():  
   selection = "You selected the option " + str(checkvar1.get())  
   label.config(text = selection)  


  
top = Tk()  
  
top.geometry("200x200")  
  
checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10,command = selection)  
  
chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn1.pack()  
  
chkbtn2.pack()  
  
chkbtn3.pack()  

label = Label(top)  
label.pack()  
  
top.mainloop()  