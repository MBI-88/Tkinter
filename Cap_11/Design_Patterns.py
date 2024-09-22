"""
Create on Jul 25 11:06:10 2021
@author: MBI

Descricion:
Script para el desarrollo del diseño con patrones.
"""
# Modulos
import tkinter as tk
from tkinter import ttk,scrolledtext,Menu

# Clases
class ButtonFactory():
    def createButton(self,type_):
        return buttonTypes[type_]() # El parentisis tambien se puede usar en la declaracion dentro\
                                    # de la lista

class ButtonBase():
    relief = 'flat'
    foreground = 'white'
    def getButtonConfig(self):
        return self.relief,self.foreground

class ButtonRide(ButtonBase):
    relief = 'ridge'
    foreground = 'red'

class ButtonSunken(ButtonBase):
    relief = 'sunken'
    foreground = 'blue'

class ButtonGroove(ButtonBase):
    relief = 'groove'
    foreground = 'green'

buttonTypes = [ButtonRide,ButtonSunken,ButtonGroove]

class WindowOOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI')
        self.createWidgets()

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text='Tab 1')
        tabControl.pack(expand=1,fill='both')
        self.monty = ttk.Labelframe(tab1,text=' Monty Python ')
        self.monty.grid(column=0,row=0,padx=8,pady=4)
        scr = scrolledtext.ScrolledText(self.monty,width=30,height=3,wrap=tk.WORD)
        scr.grid(column=0,row=3,sticky='WE',columnspan=3)
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        fileMenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='File',menu=fileMenu)
        helpMenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Help',menu=helpMenu)
        self.createButtons()

    def createButtons(self):
        factory = ButtonFactory()
        rel = factory.createButton(0).getButtonConfig()[0]
        fg = factory.createButton(0).getButtonConfig()[1]
        action = tk.Button(self.monty,text='Button '+str(0+1),relief=rel,foreground=fg)
        action.grid(column=0,row=1)

        rel = factory.createButton(1).getButtonConfig()[0]
        fg = factory.createButton(1).getButtonConfig()[1]
        action = tk.Button(self.monty,text="Button "+str(1+1),relief=rel,foreground=fg)
        action.grid(column=1,row=1)

        rel = factory.createButton(2).getButtonConfig()[0]
        fg = factory.createButton(2).getButtonConfig()[1]
        action = tk.Button(self.monty,text="Button "+str(2+1),relief=rel,foreground=fg)
        action.grid(column=2,row=1)

window = WindowOOP()
window.win.mainloop()
















