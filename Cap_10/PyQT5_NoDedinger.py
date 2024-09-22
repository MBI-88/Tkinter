# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:06:05 2021

@author: MBI
"""
# %% Modulos
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction

# %% Primera Ventana

app = QApplication(sys.argv)
gui = QWidget()
gui.setWindowTitle('PyQt5 GUI')  # Poniendo titulo a la ventana
gui.show()
sys.exit(app.exec_())


# %% Refactorizando el codigo usando orientacion a objetos

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI Class')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())


# %% QMainWindow

class Gui_MaiWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.add_widget()

    def initUI(self):
        self.setWindowTitle('PyQt5 Gui MainWindows')
        self.resize(400, 300)

    def add_widget(self):
        self.statusBar().showMessage('Text in statusbar')  # Barra de estado


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui_MaiWindows()
    gui.show()
    sys.exit(app.exec_())


# %% Aficionado una barra de menu

class GUi_menubar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.add_widget()

    def initUI(self):
        self.setWindowTitle("PyQt5 GUI menu ")
        self.resize(200, 300)

    def add_widget(self):
        self.statusBar().showMessage('Text in statusbar')
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')


app = QApplication(sys.argv)
gui = GUi_menubar()
gui.show()
sys.exit(app.exec_())


