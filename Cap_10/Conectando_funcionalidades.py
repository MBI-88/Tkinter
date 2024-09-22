"""
Created on We Jul  17 15:21:05 2021
@author: MBI
"""
# %% Modulo

import sys
from PyQt5 import QtWidgets
from MainWindow1 import Ui_MainWindow


# %% Clase

class ExitDesignerGUI():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widgets_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def widgets_actions(self):
        self.ui.actionExit.setStatusTip('Click to exit the application')
        self.ui.actionExit.triggered.connect(self.close_GUI)

    def close_GUI(self):
        self.MainWindow.close()

    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')


if __name__ == '__main__':
    ExitDesignerGUI()
