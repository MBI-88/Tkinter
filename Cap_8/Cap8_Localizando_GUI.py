# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:15:39 2021

@author: MBI
"""

#%% Librerias
import tkinter as tk 
from tkinter import ttk,scrolledtext
import pytz,datetime
from tzlocal import get_localzone
#%% Diseño de GUI

class I18N():
    def __init__(self,language):
        if language == 'en':
            self.resourceLanEnglish()
        elif language == 'de':
            self.resourceLanGerman()
        else: raise NotImplementedError('Unsupported language.')
    
    def resourceLanEnglish(self):
        self.title = "Python Grafical User Interface"
        self.file = 'File'
        self.new = 'New'
        self.help = 'Help'
        self.about = 'About'
        self.widget_label = 'Widget Frame'
        self.disabled = 'Disabled'
        self.unchecked = 'UnCheked'
        self.toggle = 'Toggle'
        self.colors = ['Blue','Gold','Red']
        self.colorIn = ['in Blue','in Gold','in Red']
        self.chooseNumber = 'Choose a number:'
        self.label2 = 'Label 2'
        self.choosename = 'Name: '
        self.Labelframe = 'Labels within a Frame'
        self.browserTo = 'Browse to file...'
        self.timeZone = "All Time Zones"
        self.localZone = 'Loacal Zone'
    
    def resourceLanGerman(self):
        self.title = "Python Grafische Benutzeroberflaeche"
        self.choosename = 'Name: '
        self.file = 'Datei'
        self.new = 'Neu'
        self.exit = 'Schliessen'
        self.help = 'Hilfe'
        self.about = 'Ueber'
        self.widget_label = 'Widgets Rahmen'
        self.disabel = 'Deaktiviert'
        self.unchecked = 'Nicht Markiert'
        self.toggle = 'Markieren'
        self.colors = ['Blau','Gold','Rot']
        self.colorIn = ['in Blau','in Gold','in Rot']
        self.Labelframe = 'Etiketten im Rahmen'
        self.chooseNumber = 'Waehle eine nummer: '
        self.label2 = 'Etikette 2'
        self.browserTo = 'Waehle eine Datei...'
        self.timeZone = 'Alle Zeitzonen'
        self.localZone = 'Lokale Zone'

class GUI():
    def __init__(self,langueje = 'en'):
        
        self.win = tk.Tk()
        self.lan = I18N(langueje)
        
        self.win.title(self.lan.title)
        self.win.resizable(False,False)
        self.create_widget()
    
    def create_widget(self):
        tabcontrol = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab1, text=self.lan.widget_label)
        tabcontrol.pack(expand=True,fill='x')
        
        submenu = ttk.Labelframe(tab1,text=self.lan.Labelframe)
        submenu.grid(column=0,row=0,sticky='W')
        ttk.Label(submenu,text=self.lan.chooseNumber).grid(column=0,row=0,sticky='W')
        self.etiqueta = tk.Label(submenu,text=self.lan.label2)
        self.etiqueta.grid(column=0,row=1,sticky='W')
        self.number = tk.StringVar()
        self.entry = ttk.Combobox(submenu,textvariable=self.number,width=15,state='readonly')
        self.entry['values'] = [val for val in range(0,20,2)]
        self.entry.grid(column=1,row=1,sticky='W')
        self.spinbox = tk.Spinbox(submenu,values=[v for v in range(10)],width=5,bd=8,relief=tk.SUNKEN,conmad=None)
        self.spinbox.grid(column=2,row=1,sticky='W')
        self.scroll = scrolledtext.ScrolledText(submenu,width=15,height=10,wrap=tk.WORD)
        self.scroll.grid(column=0,row=2,sticky='WE',columnspan=3)
        
        self.allzone = ttk.Button(submenu,text=self.lan.timeZone,command=self.getallzone)
        self.allzone.grid(column=0,row=3,sticky='WE')
        self.localzone = ttk.Button(submenu,text=self.lan.localZone,command=self.getloacalzone)
        self.localzone.grid(column=1,row=3,sticky='WE')
        self.my_time = ttk.Button(submenu,text="Time",command=self.getmaytime)
        self.my_time.grid(column=2,row=3,sticky='WE')
        
        for chile in submenu.winfo_children():
            chile.grid_configure(padx=2,pady=2)
    
    def getallzone(self):
        for tz in pytz.all_timezones:
            self.scroll.insert(tk.INSERT,tz + '\n')
    
    def getloacalzone(self):
        self.scroll.delete('1.0',tk.END)
        self.scroll.insert(tk.INSERT,get_localzone())
    
    def getmaytime(self):
        fmtStrZone = "%Y-%m-%d %H:%M:%S %Z%z"
        utc = datetime.datetime.now(pytz.timezone('UTC'))
        print(utc.strftime(fmtStrZone))
        
        la = utc.astimezone(pytz.timezone('America/Los_Angeles'))
        print(la.strftime(fmtStrZone))
        
        ny = utc.astimezone(pytz.timezone('America/New_York'))
        print(ny.strftime(fmtStrZone))
        
        self.etiqueta.configure(text=ny.strftime(fmtStrZone))
        
    
        

window = GUI('de')
window.win.mainloop()
        

#%%





