# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:24:01 2021

@author: MBI
"""
import tkinter as tk 

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