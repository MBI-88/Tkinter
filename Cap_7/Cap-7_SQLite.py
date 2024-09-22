# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:44:38 2021

@author: MBI
"""
#%% Librerias
import tkinter as tk
from tkinter import ttk,scrolledtext,messagebox
import os
import sqlite3 as sq

# %% Almacenando datos en una base MySQL via Gui

class WindSQle():
    def __init__(self)-> None:
        self.win = tk.Tk()
        self.win.title("Python GUI Database")
        self.win.iconbitmap("Media Player.ico")
        self.win.resizable(False,False)
        self.database = "My_data.db"
        self.creat_widget()
        if not os.path.exists(self.database):
            self.create_database()
    
    def creat_widget(self)-> None:
        tabcontrol = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab1,text="MySQL")
        tab2 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab2,text="Widgets")
        tabcontrol.pack(expand=1,fill='both')

        sub1 = ttk.LabelFrame(tab1,text="Python Database")
        sub1.grid(column=0,row=0,sticky="W")
        sub2 = ttk.LabelFrame(tab1,text="Book Quotation")
        sub2.grid(column=0,row=1,sticky="W")
        sub3 = ttk.LabelFrame(tab2,text="Not set")
        sub3.grid(column=0,row=0,sticky="WE")
        ttk.Label(sub3,text="Closed",foreground="red").grid(column=2,row=2,sticky="WE")
        ttk.Label(sub1,text='Book Title:',foreground="blue").grid(column=0,row=0,sticky="W")
        ttk.Label(sub1,text='Page:',foreground="blue").grid(column=1,row=0,sticky="W")
        self.booktitle_in = tk.StringVar()
        self.booktitle_get = tk.StringVar()
        self.booktitle_mody = tk.StringVar()
        self.page_in = tk.StringVar()
        self.page_get = tk.StringVar()
        self.page_mody = tk.StringVar()

        for id,etiquta in enumerate(zip((self.booktitle_in,self.booktitle_get,self.booktitle_mody),(self.page_in,self.page_get,self.page_mody)),1):
            self.entry_title = tk.Entry(sub1,textvariable=etiquta[0],width=35)
            self.entry_title.grid(column=0,row=id,sticky="W")
            self.page = tk.Entry(sub1,textvariable=etiquta[1],width=10)
            self.page.grid(column=1,row=id,sticky="W")

        for id,etiquta in enumerate(zip(("Insert Quote","Get Quote","Mody Quote"),(self.insert_quote,self.get_quote,self.mody_quote)),1):
            self.button = tk.Button(sub1,text=etiquta[0],command=etiquta[1])
            self.button.grid(column=2,row=id,sticky="W")

        self.scrolltext = scrolledtext.ScrolledText(sub2,width=45,height=20,wrap=tk.WORD)
        self.scrolltext.grid(column=0,row=0,sticky="WE",columnspan=3)

        for chi in tab1.winfo_children():
            chi.grid_configure(padx=3,pady=5)
        for i in sub1.winfo_children():
            i.grid_configure(padx=3,pady=3)

    
    def insert_quote(self):
        sql_query = """INSERT OR IGNORE INTO BOOK VALUES (NULL,?,?)"""
        sql_query_search = """SELECT ID FROM BOOK WHERE BOOK_TITLE=?"""
        sql_query_quote = "INSERT OR IGNORE INTO QUOTE_BOOK VALUES (?,?)"
        name,page = self.booktitle_in.get(),self.page_in.get()
        tupla_book = (name,int(page))
        try:
            conexion = sq.connect(self.database)
            cur = conexion.cursor()
            cur.execute(sql_query,tupla_book)
            cur.close()
            conexion.commit()
            cur = conexion.cursor()
            cur.execute(sql_query_search,(name,))
            idn = cur.fetchone()[0]
            cur.execute(sql_query_quote,(idn,self.scrolltext.get('1.0',tk.END)))# Para obtener todo el texto de scroll
            cur.close()
            conexion.commit()
            conexion.close()
            self.scrolltext.delete('1.0',tk.END) # Borra todo el texto
        except:
            messagebox.showerror("Python error..."," Cannot save data in QUOTE Table! ")
        
    def get_quote(self):
        sql_search = "SELECT * FROM QUOTE_BOOK JOIN BOOK ON QUOTE_BOOK.ID=BOOK.ID WHERE BOOK.BOOK_TITLE=?"
        name = self.booktitle_get.get()
        try:
            conexion = sq.connect(self.database)
            cur = conexion.cursor()
            cur.execute(sql_search,(name,))
            ind = cur.fetchone()[1]
            self.scrolltext.insert(tk.INSERT,ind+'\n')
            cur.close()
            conexion.commit()
            conexion.close()
        except:
            messagebox.showerror("Python error..."," Cannot get data from database! ")
        
    def mody_quote(self):
        sql_search = "SELECT ID FROM BOOK WHERE BOOK.BOOK_TITLE=?"
        sql_mody = "UPDATE QUOTE_BOOK SET QUOTE=? WHERE QUOTE_BOOK.ID=?"
        name = self.booktitle_mody.get()
        try:
            conexion = sq.connect(self.database)
            cur = conexion.cursor()
            cur.execute(sql_search,(name,))
            ind = cur.fetchone()[0]
            cur.execute(sql_mody,(self.scrolltext.get('1.0',tk.END),ind))
            cur.close()
            conexion.commit()
            conexion.close()
            self.scrolltext.delete('1.0',tk.END)
        except:
            messagebox.showerror("Python error..."," Cannot update database! ")
            

    def create_database(self)-> None:
        sql_data = """CREATE TABLE IF NOT EXISTS BOOK
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            BOOK_TITLE VARCHAR(20) UNIQUE,
            PAGE INTEGER
        )
        """
        sql_qoute = """CREATE TABLE IF NOT EXISTS QUOTE_BOOK
        (
            ID INTEGER UNIQUE,
            QUOTE VARCHAR(100)
        )
        """
        try:
            conector = sq.connect(self.database)
            cur = conector.cursor()
            cur.execute(sql_data)
            cur.execute(sql_qoute)
            cur.close()
            conector.commit()
            conector.close()
            messagebox.showinfo("Python info..."," Databes full created!")
        except:
            messagebox.showerror("Python error..."," Can't creat database!")
            
        


win = WindSQle()
win.win.mainloop()