# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:46:59 2021

@author: MBI
"""
#%% Librerias
import unittest as test 
from Cap8_CambiandoIdioma import I18N
from GUI_Refactoriced import Gui_Refactority
#%% Clase
class GuiUnites(test.TestCase):
    def testTitle(self):
        clase = I18N('en')
        self.assertEqual(clase.title,"Python Grafical User Interface")
        
    def testTitleGerman(self):
        clase = I18N('de')
        self.assertEqual(clase.title,"Python Grafische Benutzeroberflaeche")
    
class WidgetsTestsEnglish(test.TestCase):
    def setUp(self):
        self.gui = Gui_Refactority('en')
    
    def tearDown(self):
        self.gui = None
    
    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.choosename,'Name: ')
        self.assertEqual(self.gui.i18n.widget_label,'Widget Frame')
        self.assertEqual(self.gui.i18n.chooseNumber,'Choose a number:')

class WidgetsTestsGerman(test.TestCase):
    def setUp(self):
        self.gui = Gui_Refactority('de')
    
    def tearDown(self):
        self.gui = None 
        
    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.choosename,'Name: ')
        self.assertEqual(self.gui.i18n.chooseNumber,'Waehle eine nummer: ')
        self.assertEqual(self.gui.i18n.widget_label,'Widgets Rahmen')
    
    def test_nameStringVar(self):
        self.gui.name.set("Maikel")
        variable = self.gui.name.get()
        self.assertEqual(variable,"Maikel")
        
    
    def test_numberStrinVar(self):
        self.gui.number.set(1)
        variable = self.gui.number.get()
        self.assertEqual(variable,'1')
        

# Nota: Los metodos para hacer prubas deben empezar con la palabra test_<nombre deseado> es una convencion por defecto

if __name__ == '__main__':
    test.main()
#%%

        