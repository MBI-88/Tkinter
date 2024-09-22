# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:00:28 2021

@author: MBI
"""
#%% Librerias
import tkinter as tk
from tkinter import ttk,scrolledtext

#%% Cambiando de idioma

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
        


class OOP():
    def __init__(self,language = 'en'):
        self.win = tk.Tk()
        self.lang = I18N(language)
        self.win.title(self.lang.title)
        self.win.resizable(False,False)
        self.create_widget()
    
    def create_widget(self):
        tabcontrol = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab1,text=self.lang.Labelframe)
        tab2 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab2,text=self.lang.label2)
        tabcontrol.pack(expand=True,fill='both')
        
        sub1 = ttk.Labelframe(tab1,text=self.lang.widget_label)
        sub1.grid(column=0,row=0,sticky='W')
        sub2 = ttk.Labelframe(tab2,text=self.lang.help)
        sub2.grid(column=0,row=0,sticky='W')
        
        ttk.Label(sub1,text=self.lang.choosename, foreground='blue').grid(column=0,row=0,sticky='W')
        self.name = tk.StringVar()
        self.entry_name = tk.Entry(sub1,textvariable=self.name,width=35)
        self.entry_name.grid(column=0,row=1,sticky='W')
        ttk.Label(sub1,text=self.lang.chooseNumber,foreground='blue').grid(column=1,row=0,sticky='W')
        self.number = tk.StringVar()
        self.number_in = ttk.Combobox(sub1,textvariable=self.number,width=5,state='readonly')
        self.number_in.grid(column=1,row=1,sticky='W')
        self.number_in['values']= [number for number in range(1,20,2)]
        
        self.scroll = scrolledtext.ScrolledText(sub1,width=30,height=10,wrap=tk.WORD)
        self.scroll.grid(column=0,row=2,columnspan=2,sticky='WE')
        

win = OOP('en')
win.win.mainloop()


# %%
