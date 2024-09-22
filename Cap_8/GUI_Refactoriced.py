# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:22:09 2021

@author: MBI
"""
from os import path
import tkinter as tk 
from tkinter import ttk,scrolledtext
from Cap8_CambiandoIdioma import I18N
from ToolTip import ToolTip
from Logger import Logger,LogLevel
from pytz import timezone
from datetime import datetime
#%% Creando la clase refactorizada

class Gui_Refactority():
    def __init__(self,language='en'):
        self.language = language
        fullPath = path.relpath(__file__)
        self.log = Logger(fullPath)
        self.loger = LogLevel()
        print(self.log)
        self.gui = tk.Tk()
        self.i18n = I18N(self.language)
        self.gui.title(self.i18n.title)
        self.gui.iconbitmap("pyc.ico")
        self.gui.resizable(False,False)
        self.getDataTime()
        self.creat_guidget()
    
    def creat_guidget(self):
        tabcontrol = ttk.Notebook(self.gui)
        tab = ttk.Frame(tabcontrol)
        tabcontrol.add(tab,text=self.i18n.widget_label)
        tabcontrol.pack(expand=True,fill='x')
        
        subwindow = ttk.Labelframe(tab,text=self.i18n.Labelframe)
        subwindow.grid(column=0,row=0,sticky='W')
        
        self.name = tk.StringVar()
        self.name_in = tk.Entry(subwindow,textvariable=self.name,width=15)
        self.name_in.grid(column=0,row=1)
        ToolTip(self.name_in,self.i18n.choosename)
        self.number = tk.StringVar()
        self.number_in = ttk.Combobox(subwindow,textvariable=self.number,width=5,state='readonly')
        self.number_in['values'] = [valor for valor in range(1,20,2)]
        self.number_in.grid(column=1,row=1,sticky='W')
        ToolTip(self.number_in,self.i18n.chooseNumber)
        
        self.scroll = scrolledtext.ScrolledText(subwindow,width=25,height=10,wrap=tk.WORD)
        self.scroll.grid(column=0,row=3,columnspan=3,sticky='W')
        ToolTip(self.scroll," Write your note ")
        
        for chile in subwindow.winfo_children():
            chile.grid_configure(padx=4,pady=4)
    
    def getDataTime(self):
        fmtStrZone = "%Y-%m-%d %H:%M:%S %Z%z"
        utc = datetime.now(timezone('UTC'))
        self.log.writeTolog(utc.strftime(fmtStrZone),self.loger.Minimum)
        
        la = utc.astimezone(timezone('America/Los_Angeles'))
        self.log.writeTolog(la.strftime(fmtStrZone),self.loger.Normal)
        
        ny = utc.astimezone(timezone('America/New_York'))
        self.log.writeTolog(ny.strftime(fmtStrZone),self.loger.Debug)
        



if __name__ == '__main__':
    win = Gui_Refactority("de")
    print(win.log)
    win.log.writeTolog('Test message')
    win.gui.mainloop()

#%%