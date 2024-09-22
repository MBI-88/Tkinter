"""
Created on July 25 12:05:20 2021
@author: MBI

Descripcion:
Script para el desarrollo del aumento de complegidad en las GUI.
"""
# Modulos
import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, Spinbox
from sys import exit
from Clase_ToolTip import ToolTip

# Clases

class Ventana():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI')
        self.createWidgets()

    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get())

    def clearScrol(self):
        self.scr.delete('1.0', tk.END)

    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    def checkCallback(self, *ignoredArgs):
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.monty2.configure(text='Blue')
        elif radSel == 1:
            self.monty2.configure(text='Gold')
        elif radSel == 2:
            self.monty2.configure(text='Red')

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def usingGlobal(self):
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, tex='Tab 2')
        tabControl.add(tab3,text='Tab 3')

        tabControl.pack(expand=1, fill='both')

        self.monty = ttk.Labelframe(tab1, text=' Might Python')
        self.monty.grid(column=0, row=0, padx=8, pady=4)
        ttk.Label(self.monty, text='Enter a name:').grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')

        self.action = ttk.Button(self.monty, text='Click Me!', command=self.clickMe)
        self.action.grid(column=2, row=1)
        self.action = ttk.Button(self.monty, text='Clear Text',command=self.clearScrol)
        self.action.grid(column=2,row=2)
        ttk.Label(self.monty, text='Choose a number:').grid(column=1, row=0)
        number = tk.StringVar()
        numberChosen = ttk.Combobox(self.monty, width=12, textvariable=number)
        numberChosen['values'] = [1, 2, 4, 42, 100]
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)

        self.spin = Spinbox(self.monty, values=[1, 2, 4, 42, 100], width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2)

        self.scr = scrolledtext.ScrolledText(self.monty, width=30, height=3, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        self.monty2 = ttk.Labelframe(tab2, text=' Holy Grail ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.monty2, text='Disabled', variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky='W')
        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.monty2, text='Unchecked', variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky='W')
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.monty2, text='Toggle', variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky='W')

        self.chVarUn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())
        self.chVarEn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())

        colors = ['Blue', 'Gold', 'Red']
        self.radVar = tk.IntVar()
        self.radVar.set(4)

        for col in range(3):
            curRad = 'rad' + str(col)
            curRad = tk.Radiobutton(self.monty2, text=colors[col], variable=self.radVar, value=col,
                                    command=self.radCall)
            curRad.grid(column=col, row=6, sticky='W', columnspan=3)
            ToolTip(curRad, 'This is a Radiobutton control.')

        labelsFrame = ttk.Labelframe(self.monty2, text=' Labels in a Frame')
        labelsFrame.grid(column=0, row=7)
        ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
        ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)

        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=8)

        startRow = 4
        for idx in range(12):
            if idx < 2 : col = idx
            else: col += 1
            if not idx % 3: startRow += 1 ; col = 0
            b = ttk.Button(self.monty,text='Feature '+ str(idx+1))
            b.grid(column=col,row=startRow)

        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='New')
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self._quit)
        menuBar.add_cascade(label='File', menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label='About')
        menuBar.add_cascade(label='Help', menu=helpMenu)

        monty3 = ttk.Labelframe(tab3,text=' New Feature')
        monty3.grid(column=0,row=0,padx=8,pady=4)
        startRow = 4
        for idx in range(24):
            if idx < 2 : col = idx
            else: col += 1
            if not idx % 3: startRow += 1; col = 0

            b = ttk.Button(monty3,text='Feature '+str(idx+1))
            b.grid(column=col,row=startRow)

        for child in monty3.winfo_children():
            child.grid_configure(padx=8)

        self.win.iconbitmap('pyc.ico')

        strData = tk.StringVar()
        strData.set('Hello StrinVar')
        intData = tk.IntVar()
        strData = tk.StringVar()
        strData = self.spin.get()
        self.usingGlobal()
        nameEntered.focus()
        ToolTip(self.spin, 'This is a Spin control.')
        ToolTip(nameEntered, 'This is an Entry control names.')
        ToolTip(self.action, 'This is a Button control')
        ToolTip(self.scr, 'This is a ScrolledText  control.')
        ToolTip(numberChosen,'This is an Entry control  numbers.')


# Arrancando la GUI

if __name__ == '__main__':

    window = Ventana()
    window.win.mainloop()
