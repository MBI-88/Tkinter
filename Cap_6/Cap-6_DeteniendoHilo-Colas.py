# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:16:13 2021

@author: MBI
"""
#%% Librerias
import tkinter as tk
import threading as th
from tkinter import ttk,scrolledtext,filedialog,messagebox
from time import sleep
from queue import Queue
import os,shutil,socket
from socketserver import BaseRequestHandler,TCPServer
from urllib.request import urlopen
import sqlite3 as sq
#%% Deteniendo un hilo / Pasandole argumentos a un metod en un hilo

class OOPWinv2():
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
    
    def method_in_a_thread(self,nu_loops=10):
        print("Hi,how are you ?")
        for id in range(nu_loops):
            sleep(5)
            self.scrolltext.insert(tk.INSERT,str(id)+"-"+self.name.get()+"-"+self.number.get()+ '\n')
        print("method_in_a_thread(): ",self.run_thread.isAlive())

    
    def create_thread(self):
        self.run_thread = th.Thread(target=self.method_in_a_thread,args=[8])
        self.run_thread.setDaemon(True) # se usa para pasar las tareas a un segundo plano
        self.run_thread.start()
        print(self.run_thread) # Viendo la creacion del hilo
        print("createThread(): ",self.run_thread.isAlive())

win2 = OOPWinv2()
win2.win.mainloop()

# %% Como usar colas


class OOPWinv3():
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
       # self.use_queues()  si se usa esto aqui se cojela la Gui
    
    def method_in_a_thread(self,nu_loops=10):
        print("Hi,how are you ?")
        for id in range(nu_loops):
            sleep(5)
            self.scrolltext.insert(tk.INSERT,str(id)+"-"+self.name.get()+"-"+self.number.get()+ '\n')
        print("method_in_a_thread(): ",self.run_thread.isAlive())

    
    def create_thread(self):
        self.run_thread = th.Thread(target=self.method_in_a_thread,args=[5])
        self.run_thread.setDaemon(True) # se usa para pasar las tareas a un segundo plano
        self.run_thread.start()
        write_thread = th.Thread(target=self.use_queues,daemon=True)
        write_thread.start()
    
    def use_queues(self):
        gui_queue = Queue()
        print(gui_queue)
        for idx in range(10):
            gui_queue.put("Message from a queue: " + str(idx))
        
        while True:
            print(gui_queue.get())


win2 = OOPWinv3()
win2.win.mainloop()
