"""
Created on July 24 11:48:09 2021
@author: MBI
Descipcion:
Script para comparar el uso de la programacion orientada a objetos y la no orientada a objetos
La OOP es mas usada cuando nuestro codigo tiende a crecer en el futuro.
"""
#%% Modulos
import  tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext,Menu
#%% Clase

class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI')
        self.win.resizable(False,False)
        self.createWidget()

    def createWidget(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text='Tab 1')
        tabControl.pack(expand=True,fill='both')
        self.monty = ttk.LabelFrame(tab1,text=' Mighty Python')
        self.monty.grid(column=0,row=0,padx=10,pady=10)
        ttk.Label(self.monty,text='Enter a name:').grid(column=0,row=0,sticky='W')
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty,width=12,textvariable=self.name)
        nameEntered.grid(column=0,row=1,sticky='W')
        self.action = ttk.Button(self.monty,text='Click Me')
        self.action.grid(column=2,row=1)
        ttk.Label(self.monty,text='Choose a number:').grid(column=1,row=0)
        number = tk.StringVar()
        numberChosen = ttk.Combobox(self.monty,width=12,textvariable=number)
        numberChosen['values'] = (42)
        numberChosen.grid(column=1,row=1)
        numberChosen.current(0)
        scrollW = 30;scrollH = 3
        self.scr = scrolledtext.ScrolledText(self.monty,width=scrollW,height=scrollH,wrap=tk.WORD)
        self.scr.grid(column=0,row=3,sticky='WE',columnspan=3)
        menuBar = Menu(tab1)
        self.win.config(menu = menuBar)
        fileMenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='File',menu=fileMenu)
        helpMenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Help',menu=helpMenu)
        nameEntered.focus()

window = OOP()
window.win.mainloop()
#%% No Clase

def createWidget():
    tabControl = ttk.Notebook(win)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Tab 1')
    tabControl.pack(expand=True, fill='both')
    monty = ttk.LabelFrame(tab1, text=' Mighty Python')
    monty.grid(column=0, row=0, padx=10, pady=10)
    ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')
    name = tk.StringVar()
    nameEntered = ttk.Entry(monty, width=12, textvariable=name)
    nameEntered.grid(column=0, row=1, sticky='W')
    action = ttk.Button(monty, text='Click Me')
    action.grid(column=2, row=1)
    ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
    numberChosen['values'] = (42)
    numberChosen.grid(column=1, row=1)
    numberChosen.current(0)
    scrollW = 30;
    scrollH = 3
    scr = scrolledtext.ScrolledText(monty, width=scrollW, height=scrollH, wrap=tk.WORD)
    scr.grid(column=0, row=3, sticky='WE', columnspan=3)
    menuBar = Menu(tab1)
    win.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=1)
    menuBar.add_cascade(label='File', menu=fileMenu)
    helpMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label='Help', menu=helpMenu)
    nameEntered.focus()

win = tk.Tk()
win.title('Python GUI')
createWidget()
win.mainloop()