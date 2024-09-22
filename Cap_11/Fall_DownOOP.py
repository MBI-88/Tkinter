"""
Created on July 24 10:36:20 2021
@author: MBI

Descripcion:
Script para mesclar 2 estilos de codigo Fall-down y waterfall
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class  ToolTip(object):
    def __init__(self,widget,tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>',self.mouse_enter)
        widget.bind('<Leave>',self.mouse_leave)
    
    def mouse_enter(self,_event):
        self.show_tooltip()
    def mouse_leave(self,_event):
        self.hide_tooltip()
    
    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18
            
            self.tip_winow = tk.Toplevel(self.widget)
            self.tip_winow.overrideredirect(True)
            self.tip_winow.geometry("+%d+%d"%(x_left,y_top))
            
            label = tk.Label(self.tip_winow,text=self.tip_text,justify=tk.LEFT,background='#FFFFe0',relief=tk.SOLID,borderwidth=1,font=('tahoma','8','normal'))
            label.pack(ipadx=1)
    
    def hide_tooltip(self):
        if self.tip_winow:
            self.tip_winow.destroy()



win = tk.Tk()
win.title("Python GUI")
win.resizable(False,False)
lframe = ttk.Labelframe(win,text='Python Gui programing')
lframe.grid(column=0,row=0,sticky='WE',padx=10,pady=10)
ttk.Label(lframe,text='Enter a name: ').grid(column=0,row=0)
ttk.Label(lframe,text='Choose a number: ').grid(column=1,row=0,sticky='WE')
def clickMe(name,number):
    messagebox.showinfo('Information Message Box','Hello '+name+', your number is: '+number)

names = ['name0','name1','name2']
nameEntries = ['nameEntry0','nameEntry1','nameEngry2']
numbers = ['number0','number1','number2']
numberEntries = ['numberEntry0','numberEntry1','numberEntry2']

buttons = []
for idx in range(3):
    names[idx] = tk.StringVar()
    nameEntries[idx] = ttk.Entry(lframe,width=12,textvariable=names[idx])
    nameEntries[idx].grid(column=0,row=idx+1)
    nameEntries[idx].delete(0,tk.END)
    nameEntries[idx].insert(0,'<name>')
    numbers[idx] = tk.StringVar()
    numberEntries[idx] = ttk.Combobox(lframe,width=14,textvariable=numbers[idx])
    numberEntries[idx]['values'] = (1+idx,2+idx,4+idx,42+idx,100+idx)
    numberEntries[idx].grid(column=1,row=idx+1)
    numberEntries[idx].current(0)
    button = ttk.Button(lframe,text='Click Me'+str(idx),command=lambda idx=idx:clickMe(names[idx].get(),numbers[idx].get()))
    button.grid(column=2,row=idx+1,sticky=tk.W)
    buttons.append(button)
    ToolTip(nameEntries[idx],'This is an Entry widget')
    ToolTip(numberEntries[idx],'This is a DropDown')
    ToolTip(buttons[idx],'This is a Button widget')

win.mainloop()

