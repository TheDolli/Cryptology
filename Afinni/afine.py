# -*- coding: utf-8 -*-
"""
Úkol č. 2 - Afinní šifra

@author: Michaela Frodlová

1) Filtrace vstupních dat (diakritika, ošetření klíče, odstranění speciálních znaků, zachování mezer)
2) Funkce pro šifrování
3) Funkcepro dešifrování
4) GUI:     a) Pole pro zadání textu k šifrování
            b) Pole pro zadání klíče - hodnot a,b
            c) Pole pro zadání zašifrovaného textu
            d) Pole pro zobrazení zašifrované/dešifrované zprávy
"""

import sys
import unicodedata
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic
import math
from sympy import mod_inverse


qtCreatorFile = "afine.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):
    
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mod = 0
    
    def Mod(self):      
        if self.encrypt.isChecked() and self.mod == 0:
            pass
        elif self.decrypt.isChecked() and self.mod == 0:
            self.mod = 1
        elif self.decrypt.isChecked() and self.mod == 1:
            pass
        else:
            self.mod = 0
         
    def Funkce (self):
        zprava = self.textEdit.toPlainText()
        zprava_nova = zprava[:].upper()
        zprava = []
        zprava_nova = zprava_nova.replace(" ","PUIPUI")
        diakritika = unicodedata.normalize('NFKD', zprava_nova)
        diakritika = list(diakritika)
        for i in diakritika:
            if i in self.abc:
                zprava.append(i)
        a = self.spinBox_A.value()
        b = self.spinBox_B.value()
        a = int(a)
        b = int(b)
        if a == 1 and self.mod == 0:
            self.textBrowser.clear()
            self.textBrowser.append("Šifra bude velmi slabá pokud je část klíče A=1. Vyber jiné číslo.")
            self.textBrowser.show()
            return
        elif b == 0 and self.mod == 0:
            self.textBrowser.clear()
            self.textBrowser.append("Šifra bude velmi slabá pokud je část klíče B=0. Vyber jiné číslo.")
            self.textBrowser.show()
            return
        elif math.gcd(a, 26) !=1:
            self.textBrowser.clear()
            self.textBrowser.append("Část Klíče A nevyhovuje. Vyber jiné číslo!")
            self.textBrowser.show()
            return
        elif math.gcd(a, 26) !=0:
            self.textBrowser.clear()
            self.textBrowser.show()
        Sifra = []
        Desifrovano = []
        if self.mod == 0:
            for i in zprava:
                    Sifra.append(self.abc[((self.abc.index(i) * a) + b) % 26])
            Sifra_finalni = ''.join(Sifra)
            self.textBrowser.clear()
            self.textBrowser.append("".join(Sifra_finalni))
            self.textBrowser.show()
        if self.mod ==1:
            inv = mod_inverse(a, 26)
            for i in zprava:
                if i in self.abc:
                    Desifrovano.append(self.abc[(self.abc.index(i) - b) * inv % 26])
            Desifrovano_finalni = ''.join(Desifrovano)
            Desifrovano_finalni = Desifrovano_finalni.replace ("PUIPUI", " ")
            self.textBrowser.clear()
            self.textBrowser.append("".join(Desifrovano_finalni))
            self.textBrowser.show()
                    

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.go.clicked.connect(self.Funkce)
        self.encrypt.toggled.connect(self.Mod)
        self.decrypt.toggled.connect(self.Mod)
        self.textBrowser.clear()
        self.textBrowser.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
