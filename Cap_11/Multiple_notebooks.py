"""
Created on July 30 16:17:20 2021
@author:MBI
Descripcion: Script para el desarrollo de multiples notbooks
"""
import tkinter as tk
from tkinter import ttk,scrolledtext,Menu,Spinbox,messagebox
from sys import  exit

def clickMe(button,name,number):
    button.configure(text='Hello {} {}'.format(name.get(),number.get()))

def clearScrol(scr):
    scr.delete('1.0',tk.END)

def _spin(spin,scr):
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT,value + '\n')

def checkCallback(*ignored):
    pass

def create_display_area():
    display_area_label = tk.Label(display_area,text="",height=2)
    display_area_label.grid(column=0,row=0)

def clear_display_area():
    for widget in display_area.grid_slaves():
        if int(widget.grid_info()['row']) == 0:
            widget.grid_forget()

def  _quit():
    win.quit()
    win.destroy()
    exit()

def create_menu():
    menuBar = Menu(win_frame_multi_row_tabs)
    win.config(menu=menuBar)

    fileMenu = Menu(menuBar,tearoff=0)
    fileMenu.add_command(label='New')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit',command=_quit)
    menuBar.add_cascade(label='File',menu=fileMenu)

    helpMenu = Menu(menuBar,tearoff=0)
    helpMenu.add_command(label='About')
    menuBar.add_cascade(label='Help',menu=helpMenu)

def display_tab1():
    monty = ttk.Labelframe(display_area,text=' Monty Python')
    monty.grid(column=0,row=0,padx=8,pady=4)
    ttk.Label(monty,text='Enter a name:').grid(column=0,row=0,sticky='W')
    name = tk.StringVar()
    nameEntered = ttk.Entry(monty,width=12,textvariable=name)
    nameEntered.grid(column=0,row=1,sticky='W')
    ttk.Label(monty,text='Choose a number:').grid(column=1,row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(monty,width=12,textvariable=number)
    numberChosen['values'] = [1,2,4,42,100]
    numberChosen.grid(column=1,row=1)
    numberChosen.current(0)

    action = ttk.Button(monty,text='Click Me!',command=lambda:clickMe(action,name,number))
    action.grid(column=2,row=1)
    scr = scrolledtext.ScrolledText(monty,width=30,height=3,wrap=tk.WORD)
    scr.grid(column=0,row=3,sticky='WE',columnspan=3)

    spin = Spinbox(monty,values=[1,2,4,42,100],width=5,bd=8,command=lambda: _spin(spin,scr))
    spin.grid(column=0,row=2,sticky='W')
    clear = ttk.Button(monty,text='Clear Text',command=lambda:clearScrol(scr))
    clear.grid(column=2,row=2)

    startRow = 4
    for idx in range(12):
        if idx < 2: col = idx
        else: col += 1
        if not idx % 3:
            startRow += 1
            col = 0
        b = ttk.Button(monty,text='Feature '+ str(idx+1))
        b.grid(column=col,row=startRow)

def display_tab2():
    monty2 = ttk.Labelframe(display_area,text=' Holy Grail ')
    monty2.grid(column=0,row=0,padx=8,pady=4)
    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(monty2,text='Disabled',variable=chVarDis,state='disabled')
    check1.select()
    check1.grid(column=0,row=0,sticky=tk.W)
    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(monty2,text='Unchecked',variable=chVarUn)
    check2.deselect()
    check2.grid(column=1,row=0,sticky=tk.W)
    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(monty2,text='Toggle',variable=chVarEn)
    check3.deselect()
    check3.grid(column=2,row=0,sticky=tk.W)

    labelsFrame = ttk.LabelFrame(monty2,text=' Labels in a Frame ')
    labelsFrame.grid(column=0,row=7)

    ttk.Label(labelsFrame,text='Label1').grid(column=0,row=0)
    ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)

    for child in labelsFrame.winfo_children():
        child.grid_configure(padx=8)

def display_tab3():
    monty3 = ttk.LabelFrame(display_area,text=' New Feature')
    monty3.grid(column=0,row=0,padx=8,pady=4)
    startRow = 4
    for idx in range(24):
        if idx < 2: col = idx
        else: col += 1
        if not idx % 3:
            startRow += 1
            col = 0
        b = ttk.Button(monty3,text='Feature '+str(idx+1))
        b.grid(column=col,row=startRow)

    for child in monty3.winfo_children():
        child.grid_configure(padx=8)

def display_button(active_notebook,tab_no):
    btn = ttk.Button(display_area,text=active_notebook +' -Tab '+tab_no,command=lambda :messagebox.showinfo("Tab Display",'Tab: '+tab_no))
    btn.grid(column=0,row=0,padx=8,pady=8)

def notebook_callback(event):
    clear_display_area()
    current_notebook = str(event.widget)
    tab_no = str(event.widget.index('current') + 1)
    if current_notebook.endswith('notebook'):
        active_notebook = 'Notebook 1'
    elif current_notebook.endswith('notebook2'):
        active_notebook = 'Notebook 2'
    else:
        active_notebook = ''
    if active_notebook is 'Notebook 1':
        if tab_no == '1': display_tab1()
        elif tab_no == '2': display_tab2()
        elif tab_no == '3': display_tab3()
        else: display_button(active_notebook,tab_no)
    else:
        display_button(active_notebook,tab_no)

win = tk.Tk()
win.title('Python GUI')
win_frame_multi_row_tabs = ttk.Frame(win)
win_frame_multi_row_tabs.grid(column=0,row=0,sticky='W')
display_area = ttk.Labelframe(win,text=' Tab  Display Area ')
display_area.grid(column=0,row=1,sticky='WE')
note1 = ttk.Notebook(win_frame_multi_row_tabs)
note1.grid(column=0,row=0)
note2 = ttk.Notebook(win_frame_multi_row_tabs)
note2.grid(column=0,row=1)

for tab_no in range(5):
    tab1 = ttk.Frame(note1,width=0,height=0)
    tab2 = ttk.Frame(note2,width=0,height=0)
    note1.add(tab1,text=' Tab {} '.format(tab_no + 1))
    note2.add(tab2,text=' Tab {} '.format(tab_no + 1))

note1.bind("<ButtonRelease-1>",notebook_callback)
note2.bind("<ButtonRelease-1>",notebook_callback)

create_display_area()
create_menu()
display_tab1()
win.mainloop()














