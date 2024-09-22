# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:18:16 2021

@author: MBI
"""
#%% Librerias
import tkinter as tk
import threading as th
from tkinter import ttk,scrolledtext,filedialog,messagebox
from time import sleep
from queue import Queue
import os,shutil


# %% Pasando colas entre diferentes modulos

"Nota: La Gui idealmente debe ser usada para solo crear y mostrar widges y datos"
"""
El principio de codificacion de evitar dependencias innecesarias es usualmente llamado
loose coupling. Este es un principio muy importante y extremadamente recomendado
"""
# Modulo 1
class OOPWinv4():
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

        self.actionbottom = tk.Button(subwin,text="Click here",command=self.click_me)
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

    
    def create_thread(self,valor):
        self.run_thread = th.Thread(target=self.method_in_a_thread,args=[valor])
        self.run_thread.setDaemon(True) # se usa para pasar las tareas a un segundo plano
        self.run_thread.start()
        write_thread = th.Thread(target=self.use_queues,daemon=True)
        write_thread.start()
    
    def use_queues(self): # Se modifica este metodo
        while True:
            print(self.gui_queue.get())

# Modulo 2. Modulo importado 
def write_to_scrol(inst):
    print("hi from Queue ",inst)
    for idx in range(10):
        inst.gui_queue.put("Message from queue: "+ str(idx))
        
    
    inst.create_thread(6)

# Modulo 3
class POO(OOPWinv4):
    def __init__(self) -> None:
        super(POO,self).__init__()
        self.gui_queue = Queue()

    def click_me(self):
        write_to_scrol(self) # Metodo inportado del modulo 2
        
        
po = POO()

po.win.mainloop()
"""
Nota: En este ejemplo tuve que usar la herencia de clases para simular la modulacion de 
los codigos, el modulo 2 debe ser el modulo importado usando un alias segun el libro bq.
Se busca representar la eficacia de la modulacion que no es mas que separar en este caso
la representacion de widges de las operaciones logicas del software.
"""

# %% Usando dialog widgets para copiar archivos para una red

class Windows():
    def __init__(self):
        self.win = tk.Tk()
        self.win.iconbitmap("Media Player.ico")
        self.win.title("Python GUI")
        self.win.resizable(False,False)
        self.create_widgets()
        
    
    def create_widgets(self):
        tabcontrol  = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab1,text="Tab 1")
        tab2 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab2,text="Tab 2")
        tabcontrol.pack(expand=1,fill="both")

        sub1 = ttk.LabelFrame(tab1,text="Main Window")
        sub1.grid(column=0,row=0,sticky="WE")
        sub2 = ttk.LabelFrame(tab2,text="Manager Files")
        sub2.grid(column=0,row=0,sticky="W")

        ttk.Label(sub1,text="Name: ").grid(column=0,row=0,sticky="W")
        self.name = tk.StringVar()
        self.entryLeng = 24
        self.name_in = tk.Entry(sub1,width=24,textvariable=self.name)
        self.name_in.grid(column=0,row=1,sticky="W")
        self.name_in.delete(0,tk.END)
        self.name_in.insert(0,'<default name>')

        ttk.Label(sub1,text="Number: ").grid(column=1,row=0,sticky="W")
        self.number = tk.StringVar()
        self.number_in = ttk.Combobox(sub1,width=5,textvariable=self.number,state="readonly",values=[1,2,4,8,10])
        self.number_in.grid(column=1,row=1,sticky="W")
        self.number_in.current(0)

        self.actionbottom = tk.Button(sub1,text="Click here",command=self.click_me)
        self.actionbottom.grid(column=2,row=1,sticky="W")

        self.spin = tk.Spinbox(sub1,values=[1,2,4,8,10],width=5,bd=9,command=self._spin)
        self.spin.grid(column=0,row=2,sticky="W")

        self.scrolltext = scrolledtext.ScrolledText(sub1,width=15,height=8,wrap=tk.WORD)
        self.scrolltext.grid(column=0,row=3,columnspan=3,sticky="WE")
        # Tab 2
        self.lb = ttk.Button(sub2,text="Browse to file...",command=self.getFileName)
        self.lb.grid(column=0,row=0,sticky="W")
        self.file = tk.StringVar()
        self.fileEntry = ttk.Entry(sub2,width=self.entryLeng,textvariable=self.file)
        self.fileEntry.grid(column=1,row=0,sticky="W")
        self.logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(sub2,width=self.entryLeng,textvariable=self.logDir)
        self.netwEntry.grid(column=1,row=1,sticky="W")
        self.cb = ttk.Button(sub2,text="Copy file to: ",command=self.copyFile)
        self.cb.grid(column=0,row=1,sticky="W")
        for child in sub2.winfo_children():
            child.grid_configure(padx=6,pady=6)

    def click_me(self):
        self.actionbottom.configure(text="Hello "+self.name.get()+" "+self.number.get(),activebackground="blue")

    def getFileName(self):
        self.fdir = os.path.dirname(__file__)
        self.netdir = self.fdir + "/Backup"
        self.fdir = filedialog.askopenfilename(parent=self.win,initialdir=self.fdir)
        if not os.path.exists(self.netdir):
            os.makedirs(self.netdir,exist_ok=True)
        self.defaultFileEntry()
       
        
    def copyFile(self):
        src = self.fileEntry.get()
        print(src)
        file = src.split('/')[-1]
        dst = self.netwEntry.get() +'/'+ file
        try :
            shutil.copy(src,dst)
            messagebox.showinfo("Copy file to Network","Succes: File copied")
        except FileNotFoundError as err:
            messagebox.showerror("Copy file to Network","*** Failded to copy File! **\n\n"+str(err))
            
        except Exception as ex:
            messagebox.showerror("Copy file to Network",'*** Failed to copy file! **\n\n'+str(ex))

    def _spin(self):
        value = self.spin.get()
        self.scrolltext.insert(tk.INSERT,value+" "+self.name.get()+" "+self.number.get()+"\n")

    def defaultFileEntry(self):
        self.fileEntry.delete(0,tk.END)
        self.fileEntry.insert(0,self.fdir)
        if len(self.fdir) > self.entryLeng:
            self.fileEntry.config(width=len(self.fdir)+ 3)
            self.fileEntry.config(state='readonly')

        self.netwEntry.delete(0,tk.END)
        self.netwEntry.insert(0,self.netdir)
        if len(self.netdir) > self.entryLeng:
            self.netwEntry.config(width=len(self.netdir)+ 3)
            self.netwEntry.config(state='readonly')


win = Windows()
win.win.mainloop()
