#%% Administracion de diseño

import tkinter as tk 
from tkinter import ttk,scrolledtext,Menu
# %% Arregalando varias etiquetas dentro de un frame estiqueta widget

windows = tk.Tk()
windows.title("Python")
label_1 = ttk.Label(windows,text="Name")
label_1.grid(column=0,row=0)
label_2 = ttk.Label(windows,text="Number")
label_2.grid(column=1,row=0)

colors = ["Blue","Gold","Red","Green"]

name = tk.StringVar()
name_in = ttk.Entry(windows,width=12,textvariable=name)
name_in.grid(column=0,row=1)

number = tk.StringVar()
number_in = ttk.Combobox(windows,width=12,textvariable=number,state="readonly")
number_in['values'] = (1,2,4,5)
number_in.grid(column=1,row=1)
number_in.current(0)

chVardis = tk.IntVar()
chck_1= tk.Checkbutton(windows,text="Disabled",variable=chVardis,state='disabled')
chck_1.select()
chck_1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check_2 = tk.Checkbutton(windows,text="Uncheked",variable=chVarUn)
check_2.deselect()
check_2.grid(column=1,row=4,sticky=tk.W)

chaVarEn = tk.IntVar()
check_3 = tk.Checkbutton(windows,text="Enabled",variable=chaVarEn)
check_3.select()
check_3.grid(column=2,row=4,sticky=tk.W)

def redCall():
    radSel = radVar.get()
    if radSel == 0: windows.configure(background=colors[0])
    elif radSel == 1: windows.configure(background=colors[1])
    elif radSel == 2: windows.configure(background=colors[2])
    elif radSel == 3: windows.configure(background=colors[3])

radVar = tk.IntVar()
radVar.set(9)
scrol_h = 3
scrol_w = 30

for col in range(4):
    curRad = tk.Radiobutton(windows,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=5,sticky=tk.W)


text_scrol = scrolledtext.ScrolledText(windows,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,columnspan=4)

buttons_frame = ttk.LabelFrame(windows,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=7)
ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label-2").grid(column=1,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label-3").grid(column=2,row=0,sticky=tk.W)
"""
Nota: Para cambiar el orden de las etiquetas dentro de la etiqueta padre,solo usar
las propiedades de las columnas y las filas.
"""
name_in.focus()
windows.mainloop()

# %% Usando relleno de espacios alrededor de los widget
windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python")
colors = ["Blue","Gold","Red","Green"]

radVar = tk.IntVar()
radVar.set(9)
scrol_h = 3
scrol_w = 30

for col in range(4):
    curRad = tk.Radiobutton(windows,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=5,sticky=tk.W)

text_scrol = scrolledtext.ScrolledText(windows,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,columnspan=4)

buttons_frame = ttk.LabelFrame(windows,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=7,padx=20,pady=40)
ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1,sticky=tk.W)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2,sticky=tk.W)

windows.mainloop()

# %% Adicionando relleno mediante lazos
windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python")
colors = ["Blue","Gold","Red","Green"]

radVar = tk.IntVar()
radVar.set(9)
scrol_h = 3
scrol_w = 30

for col in range(4):
    curRad = tk.Radiobutton(windows,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=0,sticky=tk.W)

text_scrol = scrolledtext.ScrolledText(windows,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,columnspan=4,sticky='WE')

buttons_frame = ttk.LabelFrame(windows,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4)

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

for child in buttons_frame.winfo_children(): # Agrega un relleno en x y en y para separar las etiquetas
    child.grid_configure(padx=8,pady=4)

windows.mainloop()

# %% Expansion dinamica de la GUI usando widget
windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python GUI")
colors = ["Blue","Gold","Red","Green"]

radVar = tk.IntVar()
radVar.set(9)

for col in range(4):
    curRad = tk.Radiobutton(windows,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=0,sticky=tk.W)
# Con la propiedad sticky se alinea los widget W izquierda, E derecha; si no se pone nada lo pone en el centro
text_scrol = scrolledtext.ScrolledText(windows,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,row=1,columnspan=4)

buttons_frame = ttk.LabelFrame(windows,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4)

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

for child in buttons_frame.winfo_children(): # Agrega un relleno en x y en y para separar las etiquetas
    child.grid_configure(padx=8,pady=4)

windows.mainloop()
# %% Modificando el script anterior 
# Quitando la propiedad columnspan, hace que el widget tome el ancho de la columna donde empieza
windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python GUI")
colors = ["Blue","Gold","Red","Green"]

radVar = tk.IntVar()
radVar.set(9)

for col in range(4):
    curRad = tk.Radiobutton(windows,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=0,sticky=tk.W)
# Con la propiedad sticky se alinea los widget W izquierda, E derecha; si no se pone nada lo pone en el centro
text_scrol = scrolledtext.ScrolledText(windows,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,row=1)

buttons_frame = ttk.LabelFrame(windows,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4,sticky='W')

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

for child in buttons_frame.winfo_children(): # Agrega un relleno en x y en y para separar las etiquetas
    child.grid_configure(padx=8,pady=4)

windows.mainloop()

# %% Aliniando GUI widget por frames embebidos dentro de frames

windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python GUI")
colors = ["Blue","Gold","Red","Green"]

radVar = tk.IntVar()
radVar.set(9)

mighty = ttk.LabelFrame(windows,text="Mighty Python")
mighty.grid(column=0,row=0,padx=8,pady=4)
a_label = ttk.Label(mighty,text="Enter a name")
a_label.grid(column=0,row=0,sticky="W") # Con sticky se alinea todo el diseño de mighty

for col in range(4):
    curRad = tk.Radiobutton(mighty,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=1,sticky=tk.W)

text_scrol = scrolledtext.ScrolledText(mighty,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,row=2)

buttons_frame = ttk.LabelFrame(mighty,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4,sticky='W')

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

windows.mainloop()

# %% Creando barras de menu
def quit():
    windows.quit()
    windows.destroy()
    exit()

windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python GUI")
menu_bar = Menu(windows)
windows.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0) # Tearoff es para eliminar la linea punteada
file_menu.add_command(labe="New")
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About")


radVar = tk.IntVar()
radVar.set(9)

mighty = ttk.LabelFrame(windows,text="Mighty Python")
mighty.grid(column=0,row=0,padx=8,pady=4)
a_label = ttk.Label(mighty,text="Enter a name")
a_label.grid(column=0,row=0,sticky="W")

for col in range(4):
    curRad = tk.Radiobutton(mighty,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=1,sticky=tk.W)

text_scrol = scrolledtext.ScrolledText(mighty,width=scrol_w,height=scrol_h,wrap=tk.WORD)
text_scrol.grid(column=0,row=2)

buttons_frame = ttk.LabelFrame(mighty,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4,sticky='W')

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

windows.mainloop()
# %% Creando widget tabuladores

def radCall():
    radCell = radVar.get()
    if radCell == 0 : mighty2.configure(text=colors[0])
    if radCell == 1 : mighty2.configure(text=colors[1])
    if radCell == 2 : mighty2.configure(text=colors[2])
    if radCell == 3 : mighty2.configure(text=colors[3])


colors = ["Blue","Gold","Red","Green"]
windows = tk.Tk()
windows.title("Python GUI")
windows.resizable(False,False)
tabControl = ttk.Notebook(windows)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text="Tab_1")
tabControl.pack(expand=1,fill='both') # Hace visible los tabuladores al tamño de la ventana
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text="Tab_2")

mighty = ttk.LabelFrame(tab1,text=" Mighty Python")
mighty.grid(column=0,row=0,sticky="W")
a_label = ttk.Label(mighty,text="Enter a name")
a_label.grid(column=0,row=0,sticky="W")
ttk.Label(mighty,text="Choose a number").grid(column=1,row=0)
strinvar = tk.StringVar()
strinvar_in = tk.Entry(mighty,width=12,textvariable=strinvar)
strinvar_in.grid(column=0,row=1,sticky="W")
number = tk.StringVar()
number_in = ttk.Combobox(mighty,width=12,textvariable=number,state="readonly")
number_in["values"] = (1,4,8,10)
number_in.grid(column=1,row=1,sticky="W")
mighty2 = ttk.LabelFrame(tab2,text=" The Snake")
mighty2.grid(column=0,row=0,padx=8,pady=4,sticky="W")

chVardis = tk.IntVar()
check_1 = tk.Checkbutton(mighty2,text="Disabled",variable=chVardis,state="disabled")
check_1.deselect()
check_1.grid(column=0,row=2,sticky="W")

chaVarEn = tk.IntVar()
check_2 = tk.Checkbutton(mighty2,text="Enbled",variable=chaVarEn,state="active")
check_2.select()
check_2.grid(column=1,row=2,sticky="W")



radVar = tk.IntVar()
radVar.set(9)

for col in range(4):
    curRad = tk.Radiobutton(mighty2,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=1,sticky="W")

text_scrol = scrolledtext.ScrolledText(mighty,width=30,height=3,wrap=tk.WORD)
text_scrol.grid(column=0,row=2)


for child in mighty.winfo_children():
    child.grid_configure(padx=8)

windows.mainloop()
# %% Usando la administradion del diseño de regillas

"""
En esta seccion se analiza la potencia que tiene el grid(). En caso de que se olvide la 
asignacion de la posicion de una fila o columna par ubicar un widget tkinter lo adiciona 
automaticamente a continuacion de la fila o columna que ya esta ubicada.
"""



