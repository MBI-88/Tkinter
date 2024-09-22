"""
Created on We Jul  14 18:21:05 2021

@author: MBI
Paran convertir de .uid a .py usar : pyuic5 -x -o <name.py> <name.ui>
Parametros:
-x : hace que el modulo resultante search ejecutable
-out : especifica el nombre del archivo de salida
"""
#%% Modulos
from MainWindow1 import Ui_MainWindow
from PyQt5 import QtWidgets
#%%   Main

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
