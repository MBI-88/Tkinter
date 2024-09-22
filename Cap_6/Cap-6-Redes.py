#%% Librerias
import tkinter as tk
import threading as th
from tkinter import ttk,scrolledtext,filedialog,messagebox
from time import sleep
import shutil,socket
from socketserver import BaseRequestHandler,TCPServer
from urllib.request import urlopen


# %% Usando TCP/IP par comunicar con una red

class RequestHandler(BaseRequestHandler):
    def handle(self):
        print("Server connected to: ",self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b'Server received: ' + rsp)
    
def start_server():
    server = TCPServer(('127.0.0.1',24000),RequestHandler)
    server.serve_forever()

# %% Usando TCP/Ip continuacion

valor = 0
def write_to_scrol_TCP(inst):
    print("Hi form Queue TCP",inst)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',24000))
    for idx in range(10):
        sock.send(b'Message from a queue: '+ bytes(str(idx).encode()))
        recv = sock.recv(8192).decode()
        inst.gui_queue.put(recv)
    inst.create_thread(6)


class VentanaServer(POO): # Utiliza la herencia dle modulo Cap-6_Colas_Modulos.py
    def __init__(self)-> None:
        super(VentanaServer,self).__init__()
        self.svrt = th.Thread(target=start_server,daemon=True)
        self.svrt.start()
        self.name_in.delete(0,tk.END)
        self.name_in.insert(0,"<default>")
    
    def click_me(self):
        write_to_scrol_TCP(self)
    
    def method_in_a_thread(self,nu_loops=10):
        print("Hi,how are you ?")
        for id in range(nu_loops):
            print(id)
            sleep(3)
        print("method_in_a_thread(): ",self.run_thread.isAlive())
    
    def use_queues(self): # Se modifica este metodo
        while True:
            print(self.gui_queue.get())
            self.scrolltext.insert(tk.INSERT,self.gui_queue.get()+"\n")

ven = VentanaServer()
ven.win.mainloop()

# %% Usando urlopen para leer datos de un sitio web


def write_to_scrol(inst):
    print("hi from Queue ",inst)
    for idx in range(10):
        inst.gui_queue.put("Message from queue: "+ str(idx))

def get_html():
    try:
        http_rsp = urlopen("http://python.org")
        print(http_rsp)
        html = http_rsp.read()
        print(html)
        html_decode = html.decode()
        print(html_decode)
    except Exception as ex:
        print("** Failed to get Html! ***\n\n "+ str(ex))
    else:
        return html_decode

class Windows_HTTP(VentanaServer):
    def __init__(self):
        super(Windows_HTTP, self).__init__()
    
    def click_me(self):
        self.actionbottom.configure(text='Hello '+self.name.get())
        write_to_scrol(self)
        sleep(2)
        html_data = get_html()
        print(html_data)
        self.scrolltext.insert(tk.INSERT,html_data)
        print(self.scrolltext.get())


http = Windows_HTTP()
http.win.mainloop()

