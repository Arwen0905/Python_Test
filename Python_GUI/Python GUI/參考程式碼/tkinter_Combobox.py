# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:32:44 2020

@author: ASUS
"""


import tkinter as tk
import tkinter.ttk as ttk
top = tk.Tk()
combo = ttk.Combobox(top,value=['小明','小華','小黑', '小白']).pack()
top.mainloop()
