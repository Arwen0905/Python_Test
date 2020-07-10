# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:45:58 2020

@author: ASUS
"""

 
 
 # !/usr/bin/python3  
  
from tkinter import *  


def addlistdata():
        var=listaddEntry.get()
        listbox.insert('end',var)
        listaddEntry.delete(0,'end')
  

def deletelistdata():
    listbox.delete(listbox.curselection())

top = Tk()  
  
top.geometry("200x450")  
  
lbl = Label(top,text = "A list of favourite countries...")  
  
listbox = Listbox(top)  
  
listbox.insert(1,"India")  
  
listbox.insert(2, "USA")  
  
listbox.insert(3, "Japan")  
  
listbox.insert(4, "Austrelia")  
  
#this button will delete the selected item from the list   
  
# btn = Button(top, text = "delete", command = lambda listbox=listbox: listbox.delete(ANCHOR))  
btn = Button(top, text = "delete", command = deletelistdata)  
btn1= Button(top,text='add',command=addlistdata)
listaddEntry=Entry(top,show=None)



lbl.pack()   
listbox.pack()
listaddEntry.pack() 
btn1.pack() 
btn.pack() 
 

 
top.mainloop()  