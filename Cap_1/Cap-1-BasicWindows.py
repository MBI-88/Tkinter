# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:35:55 2021

@author: MBI
"""
#%%
import tkinter as tk 
from tkinter import ttk
#%% Primera ventana
win = tk.Tk()
win.title("Primera ventana")
win.mainloop()

#%% Creando una etiqueta
win = tk.Tk()
win.title("Primera ventana")
tk.Label(win,text='Etiqueta').grid(column=0,row=0)
win.mainloop()

#%% Adicionando botones

win = tk.Tk()
win.resizable(False,False) # Impide que se reajuste la ventana
win.title("Primera ventana")
a_label = tk.Label(win,text='Etiqueta')
a_label.grid(column=0,row=0)

def click_here():
    action.configure(text='** Hola **')
    a_label.configure(foreground='red')
    a_label.configure(text='Etiqueta roja')

action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=1,row=0)
win.mainloop()

#%% Creando caja de texto

win = tk.Tk()
win.title("Primera ventana")
a_label = tk.Label(win,text='Etiqueta')
a_label.grid(column=0,row=0)

def click_here():
    action.configure(text='Hello '+ name.get())

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)
action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=1,row=0)
win.mainloop()

#%% Opciones de foco para un widget y desabilitando widget

win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Etiqueta')
a_label.grid(column=0,row=0)

# Funcion clic_here

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)
action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=1,row=1)
name_entred.focus()
win.mainloop()

#%% Desabilitando el widget


win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Etiqueta')
a_label.grid(column=0,row=0)

# funcion click_here

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)
action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=1,row=1)
action.configure(state='disabled')
name_entred.focus()
win.mainloop()

#%% Creando combobox

win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Nombre')
a_label.grid(column=0,row=0)
b_label = ttk.Label(win,text='Numero')
b_label.grid(column=1,row=0)

def click_here():
    action.configure(text='Hello '+ name.get() +"-"+number.get())

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVardis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=2,row=1)
action.configure(state='active')
name_entred.focus()
win.mainloop()

#%% Usando boton de radio
Color1 = "Blue"
Color2 = "Gold"
Color3 = "Red"

win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Nombre')
a_label.grid(column=0,row=0)
b_label = ttk.Label(win,text='Numero')
b_label.grid(column=1,row=0)


name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVardis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=Color1)
    elif radSel == 2: win.configure(background=Color2)
    elif radSel == 3: win.configure(background=Color3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text=Color1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)

rad2 = tk.Radiobutton(win,text=Color2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3 = tk.Radiobutton(win,text=Color3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)


action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=2,row=1)
action.configure(state='active')
name_entred.focus()
win.mainloop()

#%% Usando rueda en textos
from tkinter import scrolledtext

Color1 = "Blue"
Color2 = "Gold"
Color3 = "Red"

win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Nombre')
a_label.grid(column=0,row=0)
b_label = ttk.Label(win,text='Numero')
b_label.grid(column=1,row=0)

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVardis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text=Color1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)

rad2 = tk.Radiobutton(win,text=Color2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3 = tk.Radiobutton(win,text=Color3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)

action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=2,row=1)
action.configure(state='active')

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

name_entred.focus()
win.mainloop()

# %% Adicionando mas widgets en el lazo, refactorizando el codigo anterior
colors = ["Blue","Gold","Red"]

win = tk.Tk()
win.title("Python")
a_label = tk.Label(win,text='Nombre')
a_label.grid(column=0,row=0)
b_label = ttk.Label(win,text='Numero')
b_label.grid(column=1,row=0)

name = tk.StringVar()
name_entred = tk.Entry(win,width=12,textvariable=name)
name_entred.grid(column=0,row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVardis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

def redCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=colors[0])
    elif radSel == 2: win.configure(background=colors[1])
    elif radSel == 3: win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(9) # Se establece un valor fuera del  rango de los radiobutton para que en caso de que la ventana se inicie no tome nigun rango por defecto

for col in range(3):
    curRad = tk.Radiobutton(win,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=5,sticky=tk.W)

action = tk.Button(win,text='Click here',command=click_here)
action.grid(column=2,row=1)
action.configure(state='active')

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

name_entred.focus()
win.mainloop()

# %%
