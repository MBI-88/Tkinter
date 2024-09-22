"""
Created July 25 14:10:20 2021
@author: MBI
Descipcion: Scripts para esclarece el uso de la GUI
"""
# Modulos
import tkinter as tk

# Clases
class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18

            self.tip_winow = tk.Toplevel(self.widget)
            self.tip_winow.overrideredirect(True)
            self.tip_winow.geometry("+%d+%d" % (x_left, y_top))

            label = tk.Label(self.tip_winow, text=self.tip_text, justify=tk.LEFT, background='#FFFFe0', relief=tk.SOLID,
                             borderwidth=1, font=('tahoma', '8', 'normal'))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_winow:
            self.tip_winow.destroy()