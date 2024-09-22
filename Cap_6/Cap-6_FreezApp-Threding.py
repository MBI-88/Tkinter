# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:12:46 2021

@author: MBI
"""
import tkinter as tk
import threading as th
from tkinter import ttk,scrolledtext,filedialog,messagebox
from time import sleep
from queue import Queue
import os,shutil,socket
from socketserver import BaseRequestHandler,TCPServer
from urllib.request import urlopen
import sqlite3 as sq
#%% Simulando el Freezing de una app

class OOPWin():
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.win.iconbitmap("Media Player.ico")
        self.win.resizable(False,False)
        self.create_widgets()
    
    def create_widgets(self):
        tabcontrol = ttk.Notebook(self.win)
        tab_1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab_1,text="Tab 1")
        tab_2 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab_2,text="Tab 2")
        tabcontrol.pack(expand=1,fill='both')

        subwin = ttk.LabelFrame(tab_1,text="Sub Win 1")
        subwin.grid(column=0,row=0,sticky="W")
        ttk.Label(subwin,text="Entrer Name: ").grid(column=0,row=0,sticky="W")
        self.name = tk.StringVar()
        self.name_in = tk.Entry(subwin,textvariable=self.name,width=24)
        self.name_in.grid(column=0,row=1,sticky="W")

        ttk.Label(subwin,text="Choose a number: ").grid(column=1,row=0,sticky="W")
        self.number = tk.StringVar()
        self.number_in = ttk.Combobox(subwin,width=14,textvariable=self.number,state='readonly',values=[1,2,4,42,100])
        self.number_in.grid(column=1,row=1,sticky="W")
        self.number_in.current(0)

        self.actionbottom = tk.Button(subwin,text="Click here",command=self.clickme)
        self.actionbottom.grid(column=2,row=0,sticky="W")

        self.spin = tk.Spinbox(subwin,values=[0,1,2,4,42,100],width=5,bd=9,command=self._spin)
        self.spin.grid(column=0,row=2,sticky="W")
        

        self.scrolltext = scrolledtext.ScrolledText(subwin,width=40,height=10,wrap=tk.WORD)
        self.scrolltext.grid(column=0,row=3,sticky="WE",columnspan=3)

        ttk.Label(tab_2,text="Wait for info").grid(column=0,row=0,sticky="NS")
    
    def _spin(self):
        #value = self.spin.get()
        #self.scrolltext.insert(tk.INSERT,value+" "+self.name.get()+" "+self.number.get()+"\n")
        pass

    def clickme(self):
        self.actionbottom.configure(text="Hello "+self.name.get()+" "+self.number.get(),activebackground="blue")
        for idx in range(10):
            sleep(5)
            self.scrolltext.insert(tk.INSERT,str(idx)+'\n')
    
    def method_in_a_thread(self):
        print("Hi,how are you ?")

Windows = OOPWin()
run_thead = th.Thread(target=Windows.method_in_a_thread)
Windows.win.mainloop()
#%% Arrancando el Hilo

class OOPWinv1():
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.win.iconbitmap("Media Player.ico")
        self.win.resizable(False,False)
        self.create_widgets()
    
    def create_widgets(self):
        tabcontrol = ttk.Notebook(self.win)
        tab_1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab_1,text="Tab 1")
        tab_2 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab_2,text="Tab 2")
        tabcontrol.pack(expand=1,fill='both')

        subwin = ttk.LabelFrame(tab_1,text="Sub Win 1")
        subwin.grid(column=0,row=0,sticky="W")
        ttk.Label(subwin,text="Entrer Name: ").grid(column=0,row=0,sticky="W")
        self.name = tk.StringVar()
        self.name_in = tk.Entry(subwin,textvariable=self.name,width=24)
        self.name_in.grid(column=0,row=1,sticky="W")

        ttk.Label(subwin,text="Choose a number: ").grid(column=1,row=0,sticky="W")
        self.number = tk.StringVar()
        self.number_in = ttk.Combobox(subwin,width=14,textvariable=self.number,state='readonly',values=[1,2,4,42,100])
        self.number_in.grid(column=1,row=1,sticky="W")
        self.number_in.current(0)

        self.actionbottom = tk.Button(subwin,text="Click here",command=self.clickme)
        self.actionbottom.grid(column=2,row=0,sticky="W")

        self.spin = tk.Spinbox(subwin,values=[0,1,2,4,42,100],width=5,bd=9,command=self._spin)
        self.spin.grid(column=0,row=2,sticky="W")
        

        self.scrolltext = scrolledtext.ScrolledText(subwin,width=40,height=10,wrap=tk.WORD)
        self.scrolltext.grid(column=0,row=3,sticky="WE",columnspan=3)

        ttk.Label(tab_2,text="Wait for info").grid(column=0,row=0,sticky="NS")
    
    def _spin(self):
        #value = self.spin.get()
        #self.scrolltext.insert(tk.INSERT,value+" "+self.name.get()+" "+self.number.get()+"\n")
        pass

    def clickme(self):
        self.actionbottom.configure(text="Hello "+self.name.get()+" "+self.number.get(),activebackground="blue")
        self.create_thread()
    
    def method_in_a_thread(self):
        print("Hi,how are you ?")
        for id in range(10):
            sleep(5)
            self.scrolltext.insert(tk.INSERT,str(id)+"-"+self.name.get()+"-"+self.number.get()+ '\n')

    
    def create_thread(self):
        self.run_thread = th.Thread(target=self.method_in_a_thread)
        self.run_thread.start()
        print(self.run_thread) # Viendo la creacion del hilo

win2 = OOPWinv1()
win2.win.mainloop()
"Nota: Para resolver el colapso de una app se utilizan los hilos. Se pueden trabajar  las acciones por hilos"

