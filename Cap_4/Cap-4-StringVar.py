# %% Librerias
import tkinter as tk 
from tkinter import Menu,scrolledtext,ttk
# %% Como usar la funcion StringVar()

win = tk.Tk()
win.resizable(False,False)
win.title("Pytho Gui")
doubleVar = tk.DoubleVar()
doubleVar.set(2.4)
print(doubleVar.get(),"   ",type(doubleVar))

add_doubles = 1.2222222222222222222222222 + doubleVar.get()
print(add_doubles,"   ",type(add_doubles))
print("\n")
strData = tk.StringVar()
strData.set("Hello SringVar")
print(strData.get(),"  ",type(strData.get()))
print("\n")
print(tk.IntVar()," ",tk.DoubleVar()," ",tk.BooleanVar())
"""
Nota: No  es posible obtener valores por defecto si no se usa el metodo get(), lo que se obtiene
la asignacion que tk le da a esa instancia de la variable.
"""
# %% Obtener valores desde un widget

def _spin():
    value = spin.get()
    print(value)
    sctext.insert(tk.INSERT,value + "\n")

win = tk.Tk()
win.resizable(False,False)
win.title("Python Gui")
win.iconbitmap("Media Player.ico")

tabControl = ttk.Notebook(win)
tab_1 = ttk.Frame(tabControl)
tabControl.add(tab_1,text="Tab 1")
tab_2 = ttk.Frame(tabControl)
tabControl.add(tab_2,text="Tab 2")
tabControl.pack(expand=1,fill="both")

sub_win1 = ttk.LabelFrame(tab_1,text="Sub win 1")
sub_win1.grid(column=0,row=0,sticky="W")

ttk.Label(sub_win1,text="Entry name: ").grid(column=0,row=0,sticky="W")
name = tk.StringVar()
name_entry = tk.Entry(sub_win1,width=15,textvariable=name)
name_entry.grid(column=0,row=1,sticky="W")

ttk.Label(sub_win1,text="Choose number: ").grid(column=1,row=0,sticky="W")
number = tk.StringVar()
number_entry = ttk.Combobox(sub_win1,width=5,textvariable=number,state="readonly")
number_entry["values"] = [val for val in range(0,20,2)]
number_entry.grid(column=1,row=1,sticky="W")

spin = tk.Spinbox(sub_win1,values=[val for val in range(20)],width=5,bd=8,relief=tk.GROOVE,command=_spin)
spin.grid(column=0,row=2,sticky="W")

sctext = scrolledtext.ScrolledText(sub_win1,width=30,height=4,wrap=tk.WORD)
sctext.grid(column=0,row=3,columnspan=2,sticky="W")

sub_win2 = ttk.LabelFrame(tab_2,text="Sub win 2")
sub_win2.grid(column=0,row=0,sticky="W")
ttk.Label(sub_win2,text="Wait for Entry!!").grid(column=0,row=0,sticky="W")


strData = spin.get()
print("Spinbox value: " + strData)
name_entry.focus()
win.mainloop()

# %% Usando niveles de modulos de variables globales

global_const = 42
print("Original: ",global_const)

def usingGlobal():
    print("Valor dado funcion: ",global_const)
# Efecto de el uso de la misma variable

usingGlobal()
print("Original despues de funcion: ",global_const,"\n")


def _usingGlobal():
    global_const = 77
    print("Valor dado funcion: ",global_const)
# Efecto del uso de una nueva variable local creada en la funcion

_usingGlobal()
print("Original despues de funcion: ",global_const,"\n")

def _usingGlobals():
    global global_const
    print("Original: ",global_const)
    global_const = 77
    print("Valor dado funcion: ",global_const)
# Efecto del uso de  global

_usingGlobals()
print("Original despues del cambio: ",global_const)

# %% Codificando en clases para mejorar la GUI
class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python Gui")
        self.win.resizable(False,False)
        self.win.iconbitmap("Media Player.ico")
        self.create_widget()
        ToolTip(self.win,"This is the main Windows")
    
    def clik_me(self):
        self.action.configure(text=" Hello "+self.name.get()+" "+self.number.get())
    
    def create_widget(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text="Tab 1")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2,text="Tab 2")
        tabControl.pack(expand=1,fill="both")
        sub_win1 = ttk.LabelFrame(tab1,text="Main")
        sub_win1.grid(column=0,row=0,sticky="W")
        sub_win2 = ttk.Label(tab2,text="Wait for info")
        sub_win2.grid(column=0,row=0,sticky="W")
        self.name = tk.StringVar()
        name_entry = ttk.Entry(sub_win1,width=12,textvariable=self.name)
        name_entry.grid(column=0,row=0,sticky="W")
        self.action = ttk.Button(sub_win1,text="Click me",command=self.clik_me)
        self.action.grid(column=0,row=1,sticky="W")
        self.number = tk.StringVar()
        number_entry = ttk.Combobox(sub_win1,width=5,values=[val for val in range(0,20,2)],textvariable=self.number,state="readonly")
        number_entry.grid(column=1,row=0,sticky="W")

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


oop = OOP()
oop.win
oop.win.mainloop()

# %% Escribiendo funciones de retorno

class OOP_Spin():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python Gui")
        self.win.resizable(False,False)
        self.win.iconbitmap("Media Player.ico")
        self.create_widget()

        ToolTip(self.spin,"This is spinbox")
        ToolTip(self.scrol,"This is scroltext")
        
    
    def clik_me(self):
        self.action.configure(text=" Hello "+self.name.get()+" "+self.number.get())
    
    def spin(self):
        value = self.spin.get()
        self.scrol.insert(tk.INSERT, value + "\n")
        
    def create_widget(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text="Tab 1")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2,text="Tab 2")
        tabControl.pack(expand=1,fill="both")
        sub_win1 = ttk.LabelFrame(tab1,text="Main")
        sub_win1.grid(column=0,row=0,sticky="W")
        sub_win2 = ttk.Label(tab2,text="Wait for info")
        sub_win2.grid(column=0,row=0,sticky="W")
        self.name = tk.StringVar()
        name_entry = ttk.Entry(sub_win1,width=12,textvariable=self.name)
        name_entry.grid(column=0,row=0,sticky="W")
        self.action = ttk.Button(sub_win1,text="Click me",command=self.clik_me)
        self.action.grid(column=0,row=1,sticky="W")
        self.number = tk.StringVar()
        number_entry = ttk.Combobox(sub_win1,width=5,values=[val for val in range(0,20,2)],textvariable=self.number,state="readonly")
        number_entry.grid(column=1,row=0,sticky="W")
        self.spin = tk.Spinbox(sub_win1,width=5,values=[val for val in range(10)],bd=8,relief=tk.GROOVE,command=self.spin)
        self.spin.grid(column=1,row=1,sticky="W")
        self.scrol = scrolledtext.ScrolledText(sub_win1,width=30,height=3,wrap=tk.WORD)
        self.scrol.grid(column=0,row=2,columnspan=2,sticky="W")


windows = OOP_Spin()
windows.win
windows.win.mainloop()
