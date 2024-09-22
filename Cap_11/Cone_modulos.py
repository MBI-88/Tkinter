"""
Created on Sun Jul 18 11:51:20 2021
@author:MBI

Description:
Script para demostrar el uso del conector __init__.py
"""
#%% Modulos
import tkinter as tk
from tkinter import ttk
import __init__
from MessageBox import clickMe



win = tk.Tk()
win.title("Python GUI")

lframe = ttk.Labelframe(win,text="Python GUI Programing Cookbook")
lframe.grid(column=0,row=0,sticky='WE',padx=10,pady=10)
"""def clickMe():
    messagebox.showinfo("Message Box",'Hi from same level')"""

button = ttk.Button(lframe,text="Click Me",command=clickMe)
button.grid(column=1,row=0,sticky=tk.S)
win.mainloop()