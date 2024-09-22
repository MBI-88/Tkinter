"""
Created on Sun Jul  18 11:21:05 2021
@author: MBI

Ejemplo de como hacer un codigo legible para el desarrollador
La primera seccion de codigo corresponde al erroneo y la segunda al correcto
"""
#%% Spaghetti Code #######
def PRINME(me): print(me)
import tkinter
x = y = z = 1
PRINME(z)
from tkinter import *
scrolW = 30; scrolH = 6
win = tkinter.Tk()
if x:chVarUn = tkinter.IntVar()
from tkinter import ttk
WE = 'WE'
import tkinter.scrolledtext
outputFrame = tkinter.ttk.Labelframe(win,text="Type into the scrolled text control:")
scr = tkinter.scrolledtext.ScrolledText(outputFrame,width=scrolW,height=scrolH,wrap=tkinter.WORD)

e = 'E'
scr.grid(column=1,row=1,sticky=WE,padx=8)
outputFrame.grid(column=0,row=2,sticky=e,padx=8)
lFrame = None
if y:chck2 = tkinter.Checkbutton(lFrame,text="Enabled",variable=chVarUn)
wE = 'WE'
if y==x:PRINME(x)
lFrame=tkinter.ttk.Labelframe(win,text='Spaghetti')
chck2.grid(column=1,row=4,sticky=tkinter.W,columnspan=3)
PRINME(z)
lFrame.grid(column=0,row=0,sticky=wE,padx=10,pady=10)
chck2.select()
try:win.mainloop()
except : PRINME(x)
chck2.deselect()
if y==x:PRINME(x)
#%% Diseño correcto del codigo
# =============================
# Imports
# =============================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# ==============================
# Crando Instancias
# ==============================
win = tk.Tk()
# ==============================
# Adicionando Titulo
# =============================
win.title('Python Gui')
# =============================
# Desabilitando el reajuste de ventana
# =============================
win.resizable(False,False)
# =============================
# Adicionando una Etiqueta,caja de texto, caja combo
# ==============================
lFrame = ttk.Labelframe(win,text='Python GUI Programing Cookboook')
lFrame.grid(column=0,row=0,sticky='WE',padx=10,pady=10)
# ==============================
# Usando el control de texto deslisabel
# ==============================
outputFrame = ttk.Labelframe(win,text='Type into the scrolled text control: ')
outputFrame.grid(column=0,row=2,sticky='E',padx=8)
scrolW = 30
scrolH = 6
scr = scrolledtext.ScrolledText(outputFrame,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=1,row=0,sticky='WE')
# ============================
# Creando un boton de chequeo
# ============================
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(lFrame,text='Enabled',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W,columnspan=3)
#=============================
# Corriendo la Ventana
# ============================
win.mainloop()

















