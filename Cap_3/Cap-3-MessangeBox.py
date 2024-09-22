# %% 
import tkinter as tk 
from tkinter import ttk,Menu,messagebox,scrolledtext
# %% Creando cajas de mensajes,informacion,alerta y error

def msgBox():
    messagebox.showinfo("Python Message info Box","A Python GUI creaded using tkinter:\nThe year is 2021")
    #messagebox.showwarning("Python Message Warning Box","A Python Gui created using tkinter:\nWarning: There might be a bug in this code")
    #messagebox.showerror("Python Message Error Box","A Python Gui created using tkinter:\nError: Houston ~ we Do have a serios Problem!")
def quit():
    windows.quit()
    windows.destroy()
    exit()

def redCall():
    radSel = radVar.get()
    if radSel == 0: windows.configure(background=colors[0])
    elif radSel == 1: windows.configure(background=colors[1])
    elif radSel == 2: windows.configure(background=colors[2])
    elif radSel == 3: windows.configure(background=colors[3])

colors = ["Blue","Gold","Red","Green"]
windows = tk.Tk()
windows.resizable(False,False)
windows.title("Python GUI")
menu_bar = Menu(windows)
windows.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0) # Tearoff es para eliminar la linea punteada
file_menu.add_command(label="New")
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
help_menu = Menu(menu_bar,tearoff=0)
help_menu.add_command(label="About",command=msgBox)
menu_bar.add_cascade(label="Help",menu=help_menu)



radVar = tk.IntVar()
radVar.set(9)

mighty = ttk.LabelFrame(windows,text="Mighty Python")
mighty.grid(column=0,row=0,padx=8,pady=4)
a_label = ttk.Label(mighty,text="Enter a name")
a_label.grid(column=0,row=0,sticky="W")

for col in range(4):
    curRad = tk.Radiobutton(mighty,text=colors[col],variable=radVar,value=col,command=redCall)
    curRad.grid(column=col,row=1,sticky=tk.W)

text_scrol = scrolledtext.ScrolledText(mighty,width=30,height=3,wrap=tk.WORD)
text_scrol.grid(column=0,row=2)

buttons_frame = ttk.LabelFrame(mighty,text=" Labels in a Frame ")
buttons_frame.grid(column=0,row=4,sticky='W')

ttk.Label(buttons_frame,text="Label-1").grid(column=0,row=0)
ttk.Label(buttons_frame,text="Label-2").grid(column=0,row=1)
ttk.Label(buttons_frame,text="Label-3").grid(column=0,row=2)

windows.mainloop()

# %% Caja de  mensajes brindando opciones

def _msgBox():
    answer = messagebox.askyesnocancel("Python Message Multi Choice Box","Are you sure really wish to do this?")
    print(answer)

windows = tk.Tk()
windows.title("Python Gui")
windows.resizable(False,False)
menu_bar = Menu(windows)
windows.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0) # Tearoff es para eliminar la linea punteada
file_menu.add_command(labe="New")
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
help_menu = Menu(menu_bar,tearoff=0)
help_menu.add_command(label="About",command=_msgBox)
help_menu.add_command(label='Info',command=msgBox)
menu_bar.add_cascade(label="Help",menu=help_menu)

windows.mainloop()

# %% Creando cajas de mensajes independientes
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Python Message","Python Gui created using tkinter:\nThe year is 2021")



# %% Creando el titulo de la ventana tkinter

win  = tk.Tk()
win.title("Python GUI")
win.resizable(False,False)
win.mainloop()

# %% Cambiando el icono de la ventana principal

win = tk.Tk()
win.title("Python GUI")
win.iconbitmap("Media Player.ico")
win.mainloop()

# %% Usando caja de control spin

def _spin():
    value = spin.get()
    #print(value) # Es para imprimir en consola
    text_scrol.insert(tk.INSERT,value +'\n')

windows = tk.Tk()
windows.title("Python GUI")
windows.iconbitmap("Media Player.ico")
windows.resizable(False,False)
tabControl = ttk.Notebook(windows)
tab_1 = ttk.Frame(tabControl)
tabControl.add(tab_1,text="Tab-1")
tabControl.pack(expand=1,fill="both")
tab_2 = ttk.Frame(tabControl)
tabControl.add(tab_2,text="Tab-2")

subwindo = ttk.LabelFrame(tab_1,text="")
subwindo.grid(column=0,row=0,sticky="W")
label1 = ttk.Label(subwindo,text="Enter name")
label1.grid(column=0,row=0,sticky="W")
label2 = ttk.Label(subwindo,text="Choose number")
label2.grid(column=1,row=0,sticky="W")

name = tk.StringVar()
na_choosed = tk.Entry(subwindo,width=10,textvariable=name)
na_choosed.grid(column=0,row=1,sticky="W")
number = tk.StringVar()
nu_choosed = ttk.Combobox(subwindo,width=10,textvariable=number,state="readonly")
nu_choosed["values"] = [1,2,3,4,5]
nu_choosed.grid(column=1,row=1,sticky="W")

"""
Opciones para el uso de Spinbox : 
width: ajustar el ancho
bd: reajusta los bordes, se importa directamente de tkinter
values : se puede establecer un set de valores a elegir a demas de un rango 
rago: se puede usar un rango (from_ , to), estas son variables separadas lo contrario de values

Para ajustar el estilo de los Spinbox se usa el parametro relief:
.tk.SUNKEN, es la opcion por defecto
.tk.RAISED
.tk.FLAT
.tk.GROOVE
.tk.RIDGE

"""
spin = tk.Spinbox(subwindo,values=[1,2,4,10,40,100],width=5,bd=8,relief=tk.GROOVE,command=_spin)
spin.grid(column=0,row=2,sticky="W")

text_scrol = scrolledtext.ScrolledText(subwindo,width=30,height=3,wrap=tk.WORD)
text_scrol.grid(column=0,row=3,columnspan=2,sticky="W")


windows.mainloop()

# %% Creando tips de ayudas

windows = tk.Tk()
windows.title("Python GUI")
windows.iconbitmap("Media Player.ico")
windows.resizable(False,False)
menu_bar = Menu(windows)
windows.config(menu=menu_bar)
menu_bar.add_cascade(label="File")
menu_bar.add_cascade(label="Help")
tabControl = ttk.Notebook(windows)
tab_1 = ttk.Frame(tabControl)
tabControl.add(tab_1,text="Tab_1")
tabControl.pack(expand=1,fill="both")
tab_2 = ttk.Frame(tabControl)
tabControl.add(tab_2,text="Tab_2")

subwindo = ttk.LabelFrame(tab_1,text="")
subwindo.grid(column=0,row=0,sticky="W")
label1 = ttk.Label(subwindo,text="Enter name")
label1.grid(column=0,row=0,sticky="W")
label2 = ttk.Label(subwindo,text="Choose number")
label2.grid(column=1,row=0,sticky="W")

name = tk.StringVar()
na_choosed = tk.Entry(subwindo,width=10,textvariable=name)
na_choosed.grid(column=0,row=1,sticky="W")
number = tk.StringVar()
nu_choosed = ttk.Combobox(subwindo,width=10,textvariable=number,state="readonly")
nu_choosed["values"] = [1,2,3,4,5]
nu_choosed.grid(column=1,row=1,sticky="W")

class ToolTip():
    def __init__(self,widget,tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind("<Enter>",self.mouse_enter)
        widget.bind("<Leave>",self.mouse_leave)
    
    def mouse_enter(self,_event):
        self.show_tooltip()
    def mouse_leave(self,_event):
        self.hide_tooltip()
    
    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 15
            self.tip_window = tk.Toplevel(self.widget)
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d"%(x_left,y_top))
            label = tk.Label(self.tip_window,text=self.tip_text,
            justify=tk.LEFT,background = "#ffffe0",relief = tk.SOLID,
            borderwidth=1, font=("tahoma","8","normal"))
            label.pack(ipadx=1)
    
    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()


spin = tk.Spinbox(subwindo,values=[1,2,3,4,10,100],width=5,bd=9,relief=tk.GROOVE,command=_spin)
spin.grid(column=0,row=2)
ToolTip(spin,"This is a Spin control")

text_scrol = scrolledtext.ScrolledText(subwindo,width=30,height=3,wrap=tk.WORD)
text_scrol.grid(column=0,row=3,sticky="WE",columnspan=2)
ToolTip(text_scrol,"This si a ScrolledText widget")

windows.mainloop()

# %% Adicionando barra de progreso
from time import sleep

def radCall():
    value = radVar.get()
    if value == 0: subwindo.configure(text=colors[0])
    if value == 1:subwindo.configure(text=colors[1])
    if value == 2:subwindo.configure(text=colors[2])

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()

    progress_bar["value"] = 0

def start_progessbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms,progress_bar.stop)


colors = ["Red","Blue","Green"]
win = tk.Tk()
win.title("Python GUI")
win.resizable(False,False)
win.iconbitmap("Media Player.ico")

tabControl = ttk.Notebook(win)
tab_1 = ttk.Frame(tabControl)
tab_1.grid(padx=4,pady=8)
tabControl.add(tab_1,text="Tab_1")
tab_2 = ttk.Frame(tabControl)
tab_2.grid(padx=4,pady=8)
tabControl.add(tab_2,text="Tab_2")
tabControl.pack(expand=1,fill="both")
subwindo = ttk.LabelFrame(tab_1,text="")
subwindo.grid(column=0,row=0,sticky="WE")

radVar = tk.IntVar()
radVar.set(5)

for col in range(3):
    curRad = tk.Radiobutton(subwindo,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=1,sticky=tk.W)

progress_bar = ttk.Progressbar(tab_1,orient='horizontal',length=286,mode='determinate')
progress_bar.grid(column=0,row=3,pady=2,sticky="WE")

buttons_frame = ttk.LabelFrame(subwindo,text="ProgressBar")
buttons_frame.grid(column=0,row=2,sticky="W",columnspan=2)
ttk.Button(buttons_frame,text=" Run Progressbar ",command=run_progressbar).grid(column=0,row=0,sticky="W")
ttk.Button(buttons_frame,text=" Start Progressbar ",command=start_progessbar).grid(column=0,row=1,sticky="W")
ttk.Button(buttons_frame,text=" Stop immediately ",command=stop_progressbar).grid(column=0,row=2,sticky="W")
ttk.Button(buttons_frame,text=" Stop after second ",command=progressbar_stop_after).grid(column=0,row=3,sticky="W")

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2,pady=1)

for child in subwindo.winfo_children():
    child.grid_configure(padx=2,pady=2)


win.mainloop()

# %% Como usar Canvas widget

ventana = tk.Tk()
ventana.resizable(False,False)
ventana.title("Python Gui")
ventana.iconbitmap("Media Player.ico")

tabControl = ttk.Notebook(ventana)
tab_1 = ttk.Frame(tabControl)
tab_1.grid(padx=8,pady=4)
tabControl.add(tab_1,text="Tab 1")

tab_2 = ttk.Frame(tabControl)
tab_2.grid(padx=8,pady=4)
tabControl.add(tab_2,text="Tab 2")

tab_3 = ttk.Frame(tabControl)
tab_3.grid(padx=8,pady=4)
tabControl.add(tab_3,text="Tab 3")
tabControl.pack(expand=1,fill="both")

subventana_1 = ttk.LabelFrame(tab_1,text="Sub ventana 1")
subventana_1.grid(column=0,row=0,sticky="W")
ttk.Label(subventana_1,text="Entra el nombre: ").grid(column=0,row=0,sticky="W")
entry = tk.StringVar()
entred = tk.Entry(subventana_1,width=15,textvariable=entry)
entred.grid(column=1,row=0,sticky="E")

subventana_2 = ttk.LabelFrame(tab_2,text="Sub ventana 2")
subventana_2.grid(column=0,row=0,sticky="W")
ttk.Label(subventana_2,text="Elige un numero: ").grid(column=0,row=0,sticky="W")
number = tk.StringVar()
nu_choosed = ttk.Combobox(subventana_2,width=10,textvariable=number,state="readonly")
nu_choosed["values"] = [1,2,3,4,5]
nu_choosed.grid(column=1,row=0,sticky="E")

subventana_3 = tk.Frame(tab_3,bg="blue")
subventana_3.pack()
for orannge_color in range(2):
    canvas = tk.Canvas(subventana_3,width=150,height=80,highlightthickness=0,bg='orange')
    canvas.grid(row=orannge_color,column=orannge_color)

ventana.mainloop()
