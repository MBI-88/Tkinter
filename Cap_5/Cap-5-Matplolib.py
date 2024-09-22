# %% Librerias
import tkinter as tk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# %% Planos Matplotlib

x_values = [1,2,3,4]
y_values = [5,7,6,8]
plt.plot(x_values,y_values)
plt.show()
# %% Ubicando etiquetas sobre el plano
 
fig = Figure(figsize=(12,8),facecolor='white')
axis = fig.add_subplot(111)

xvalues = [1,2,3,4]
yvalues = [5,7,6,8]

axis.plot(xvalues, yvalues)
axis.set_xlabel("Horizontal Label")
axis.grid(linestyle='-')

def destroy():
    root.quit()
    root.destroy()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW',destroy)
canvas = FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)

root.mainloop()

# %% Usando mas imagenes

fig = Figure(figsize=(12,8),facecolor='white')

axis1 = fig.add_subplot(221)
axis2 = fig.add_subplot(222,sharex=axis1,sharey=axis1)
axis3 = fig.add_subplot(223,sharex=axis1,sharey=axis1)

axis1.plot(xvalues,yvalues)
axis1.set_xlabel("Horizontal Label 1")
axis1.set_ylabel("Vertical Label 1")
axis1.grid(linestyle='-')

axis2.plot(xvalues,yvalues)
axis2.set_xlabel("Horizontal Label 2")
axis2.set_ylabel("Vertical Label 2")
axis2.grid(linestyle='-')

axis3.plot(xvalues,yvalues)
axis3.set_xlabel("Horizontal Label 3")
axis3.set_ylabel("Vertical Label 3")
axis3.grid(linestyle='-')

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW',destroy)
root.title("Python Gui matplotlib")
root.resizable(False,False)
root.iconbitmap("Python_GUI/Cap_5/Media Player.ico")
canvas = FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)

root.mainloop()

# %% Dandole una leyenda

fig = Figure(figsize=(12,5),facecolor='white')
axis = fig.add_subplot(111)

xvalues = [1,2,3,4]
yvalues0 = [6,7.5,8,7.5]
yvalues1 = [5.5,6.5,8,6]
yvalues2 = [6.5,7,8,7]

t0, = axis.plot(xvalues,yvalues0,color="red") # Si se quitan las comas se pierde la leyenda del ploteo en cuestion
t1, = axis.plot(xvalues,yvalues1,color="green") # de lo contrario hay que desempaquetar la salida del ploteo
t2, = axis.plot(xvalues,yvalues2,color="purple") 

axis.set_ylabel("Vertical Label")
axis.set_xlabel("Horizontal Label")
axis.grid()
fig.legend((t0,t1,t2),('First line','Second line','Third'),"upper right")

def _destroyWindows():
    root.quit()
    root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW",_destroyWindows)
root.title("Python Gui Matplotlib")
root.iconbitmap("Media Player.ico")
root.resizable(False,False)

canvas = FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tk.TOP,fill="both",expand=1)

root.mainloop()

# %% Esclando la grafica

fig = Figure(figsize=(12,5),facecolor="white")
axis = fig.add_subplot(111)
yvalues0 = [6,7.5,8,7.5]
yvalues1 = [5.5,6.5,50,6]
yvalues2 = [6.5,7,8,7]

t0, = axis.plot(xvalues,yvalues0,color='red')
t1, = axis.plot(xvalues,yvalues1,color='gray')
t2, = axis.plot(xvalues,yvalues2,color='blue')
axis.grid(linestyle='--')
axis.set_ylim(5,8)
fig.legend((t0,t1,t2),('First line','Second line','Third'),"upper right")

win = tk.Tk()
win.protocol("WM_DEDETE_WINDOW",_destroyWindows)
win.title("Python Gui Scaling Matplotlib")
win.iconbitmap("Python_GUI/Cap_5/Media Player.ico")
win.resizable(False,False)

canvas = FigureCanvasTkAgg(fig,master=win)
canvas._tkcanvas.pack(side="top",fill="both",expand=1)

win.mainloop()

# %% Austando la escala de la grafica

fig = Figure(figsize=(12,5),facecolor="white")
axis = fig.add_subplot(111)
yvalues0 = [6,7.5,8,7.5]
yvalues1 = [5.5,6.5,50,6]
yvalues2 = [6.5,7,8,7]

t0, = axis.plot(xvalues,yvalues0,color='red')
t1, = axis.plot(xvalues,yvalues1,color='gray')
t2, = axis.plot(xvalues,yvalues2,color='blue')
axis.grid(linestyle='--')
axis.set_xlim(0,8)
axis.set_ylim(0,8)
fig.legend((t0,t1,t2),('First line','Second line','Third'),"upper right")

win = tk.Tk()
win.protocol("WM_DEDETE_WINDOW",_destroyWindows)
win.title("Python Gui Scaling Matplotlib")
win.iconbitmap("Media Player.ico")
win.resizable(False,False)

canvas = FigureCanvasTkAgg(fig,master=win)
canvas._tkcanvas.pack(side="top",fill="both",expand=1)

win.mainloop()

# %% Ajuste dinamico

fig = Figure(figsize=(12,5),facecolor="white")
axis = fig.add_subplot(111)
yvalues0 = [6,7.5,8,7.5]
yvalues1 = [5.5,6.5,50,6]
yvalues2 = [6.5,7,8,7]

t0, = axis.plot(xvalues,yvalues0,color='red')
t1, = axis.plot(xvalues,yvalues1,color='gray')
t2, = axis.plot(xvalues,yvalues2,color='blue')
axis.grid(linestyle='--')

yall = [yvalues0,yvalues1,yvalues2]
minY = min([y for yval in yall for y in yval])
maxY = max([y for yval in yall for y in yval if y < 20])

axis.set_xlim(min(xvalues),max(xvalues))
axis.set_ylim(minY,maxY)
fig.legend((t0,t1,t2),("Line 1","Line 2","Line 3"),"upper right")

win = tk.Tk()
win.title("Python Gui Auto Sacling Matplolib")
win.iconbitmap("Media Player.ico")
win.resizable(False,False)
win.protocol("WM_DEDETE_WINDOWS",_destroyWindows)

base = FigureCanvasTkAgg(fig,master=win)
base._tkcanvas.pack(side="top",fill="both",expand=1)

win.mainloop()

# %%
