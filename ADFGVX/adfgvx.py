# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:04:06 2018

Úkol č. 4 - Šifra ADFG(V)X

@author: Michaela Frodlová

1) Správná funkce vstupních dat (Zachování mezer, odstranění diakritiky apod.)
2) Vygenerování náhodné abecedy pro ADFG(V)X
3) ADFGX a ADFGVX šifrování
4) ADFGX a ADFGVX dešifrování
5) GUI  - Pole pro zadání textu pro šifrování/dešifrování
        - Pole pro zadání klíče
        - Pole pro zadání šifrovací matice ručně spolu s vyřazováním, či znázorněním zbývajících znaků pro vyplnění
        - Výpis zašifrovaného textu ( mezery dle sloupců)
        - Výpis aktuální šifrovací tabulky
        - Tlačítko pro volbu šifrování/dešifrování v rámcistejného GUI
        - Přepínač pro volbu verze ADFGX/ADFGVX (CZ/EN verze )
        - Přepínač pro volbu zadání matice a náhodného generování
"""

import sys
import random
import unicodedata
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

qtCreatorFile = "adfgvx.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):
    
    adfgvx_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    en_abc = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    cz_abc = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    rand_abc = []
    abc = adfgvx_abc
    VelikostMatice = 0
    abcVlastni = []
    
    def VyberABC(self):
        
        if self.ADFGVX.isChecked():
            self.abc=self.adfgvx_abc
            self.pushButton_Sifruj.setEnabled(True)
            self.pushButton_Desifruj.setEnabled(True)
            self.VelikostMatice=0
            self.ran1.setText("")
            self.ran2.setText("")
            self.CZ.setEnabled(False)
            self.EN.setEnabled(False)
            self.L01.setText("A")
            self.L02.setText("B")
            self.L03.setText("C")
            self.L04.setText("D")
            self.L05.setText("E")
            self.L06.setText("F")
            self.L07.setText("G")
            self.L08.setText("H")
            self.L09.setText("I")
            self.L10.setText("J")
            self.L11.setText("K")
            self.L12.setText("L")
            self.L13.setText("M")
            self.L14.setText("N")
            self.L15.setText("O")
            self.L16.setText("P")
            self.L17.setText("Q")
            self.L18.setText("R")
            self.L19.setText("S")
            self.L20.setText("T")
            self.L21.setText("U")
            self.L22.setText("V")
            self.L23.setText("W")
            self.L24.setText("X")
            self.L25.setText("Y")
            self.L26.setText("Z")
            self.L27.setText("0")
            self.L28.setText("1")
            self.L29.setText("2")
            self.L30.setText("3")
            self.L31.setText("4")
            self.L32.setText("5")
            self.L33.setText("6")
            self.L34.setText("7")
            self.L35.setText("8")
            self.L36.setText("9")
            self.P1R.setText("A")
            self.P2R.setText("D")
            self.P3R.setText("F")
            self.P4R.setText("G")
            self.P5R.setText("V")
            self.P6R.setText("X")
            self.P1S.setText("A")
            self.P2S.setText("D")
            self.P3S.setText("F")
            self.P4S.setText("G")
            self.P5S.setText("V")
            self.P6S.setText("X")
            self.push_0.setEnabled(True)
            self.push_1.setEnabled(True)
            self.push_2.setEnabled(True)
            self.push_3.setEnabled(True)
            self.push_4.setEnabled(True)
            self.push_5.setEnabled(True)
            self.push_6.setEnabled(True)
            self.push_7.setEnabled(True)
            self.push_8.setEnabled(True)
            self.push_9.setEnabled(True)
            self.W.setEnabled(True)
            self.J.setEnabled(True)
            if self.VelikostMatice == 0:
                self.abc=self.adfgvx_abc
            elif self.VelikostMatice ==1:
                self.VelikostMatice=0
                self.abc=self.adfgvx_abc
            elif self.VelikostMatice ==2:
                self.VelikostMatice=0
                self.abc=self.cz_abc
        if self.ADFGX.isChecked():
            self.pushButton_Sifruj.setEnabled(True)
            self.pushButton_Desifruj.setEnabled(True)
            self.abc=self.cz_abc
            self.CZ.isChecked()
            self.ran1.setText("")
            self.ran2.setText("")
            self.CZ.setEnabled(True)
            self.EN.setEnabled(True)
            if self.CZ.isChecked():
                self.abc=self.cz_abc
                self.pushButton_Sifruj.setEnabled(True)
                self.pushButton_Desifruj.setEnabled(True)
                self.VelikostMatice=1
                self.ran1.setText("")
                self.ran2.setText("")
                self.P5S.setText("X")
                self.P6S.setText(" ")
                self.P5R.setText("X")
                self.P6R.setText(" ")
                self.L31.setText(" ")
                self.L32.setText(" ")
                self.L33.setText(" ")
                self.L34.setText(" ")
                self.L35.setText(" ")
                self.L36.setText(" ")
                self.L06.setText(" ")
                self.L12.setText(" ")
                self.L18.setText(" ")
                self.L24.setText(" ")
                self.L30.setText(" ")
                self.L01.setText("A")
                self.L02.setText("B")
                self.L03.setText("C")
                self.L04.setText("D")
                self.L05.setText("E")
                self.L07.setText("F")
                self.L08.setText("G")
                self.L09.setText("H")
                self.L10.setText("I")
                self.L11.setText("J")
                self.L13.setText("K")
                self.L14.setText("L")
                self.L15.setText("M")
                self.L16.setText("N")
                self.L17.setText("O")
                self.L19.setText("P")
                self.L20.setText("Q")
                self.L21.setText("R")
                self.L22.setText("S")
                self.L23.setText("T")
                self.L25.setText("U")
                self.L26.setText("V")
                self.L27.setText("X")
                self.L28.setText("Y")
                self.L29.setText("Z")
                self.push_0.setEnabled(False)
                self.push_1.setEnabled(False)
                self.push_2.setEnabled(False)
                self.push_3.setEnabled(False)
                self.push_4.setEnabled(False)
                self.push_5.setEnabled(False)
                self.push_6.setEnabled(False)
                self.push_7.setEnabled(False)
                self.push_8.setEnabled(False)
                self.push_9.setEnabled(False)
                self.W.setEnabled(False)
                self.J.setEnabled(True)
                if self.VelikostMatice ==0:
                    self.abc=self.cz_abc
                    self.VelikostMatice=1
                elif self.VelikostMatice ==1:
                    self.abc=self.cz_abc
                elif self.VelikostMatice ==2:
                    self.abc=self.cz_abc
                    self.VelikostMatice=1
            elif self.EN.isChecked():
                self.abc=self.en_abc
                self.pushButton_Sifruj.setEnabled(True)
                self.pushButton_Desifruj.setEnabled(True)
                self.VelikostMatice=2
                self.ran1.setText("")
                self.ran2.setText("")
                self.P5S.setText("X")
                self.P6S.setText(" ")
                self.P5R.setText("X")
                self.P6R.setText(" ")
                self.L31.setText(" ")
                self.L32.setText(" ")
                self.L33.setText(" ")
                self.L34.setText(" ")
                self.L35.setText(" ")
                self.L36.setText(" ")
                self.L06.setText(" ")
                self.L12.setText(" ")
                self.L18.setText(" ")
                self.L24.setText(" ")
                self.L30.setText(" ")
                self.L01.setText("A")
                self.L02.setText("B")
                self.L03.setText("C")
                self.L04.setText("D")
                self.L05.setText("E")
                self.L07.setText("F")
                self.L08.setText("G")
                self.L09.setText("H")
                self.L10.setText("I")
                self.L11.setText("K")
                self.L13.setText("L")
                self.L14.setText("M")
                self.L15.setText("N")
                self.L16.setText("O")
                self.L17.setText("P")
                self.L19.setText("Q")
                self.L20.setText("R")
                self.L21.setText("S")
                self.L22.setText("T")
                self.L23.setText("U")
                self.L25.setText("V")
                self.L26.setText("W")
                self.L27.setText("X")
                self.L28.setText("Y")
                self.L29.setText("Z")
                self.push_0.setEnabled(False)
                self.push_1.setEnabled(False)
                self.push_2.setEnabled(False)
                self.push_3.setEnabled(False)
                self.push_4.setEnabled(False)
                self.push_5.setEnabled(False)
                self.push_6.setEnabled(False)
                self.push_7.setEnabled(False)
                self.push_8.setEnabled(False)
                self.push_9.setEnabled(False)
                self.J.setEnabled(False)
                self.W.setEnabled(True)
                if self.VelikostMatice ==0:
                    self.abc=self.en_abc
                    self.VelikostMatice=2
                elif self.VelikostMatice ==1:
                    self.VelikostMatice ==2
                    self.abc=self.en_abc
                elif self.VelikostMatice ==2:
                    self.abc=self.en_abc

    def RandomABC(self):
        self.pushButton_Sifruj.setEnabled(True)
        self.pushButton_Desifruj.setEnabled(True)
        if self.VelikostMatice==1:
            shufabc=list(self.cz_abc)
            random.shuffle(shufabc)
            vypln= ''.join(shufabc)
            self.rand_abc=vypln
            self.abc=self.rand_abc
            self.L01.setText(vypln[0])
            self.L02.setText(vypln[1])
            self.L03.setText(vypln[2])
            self.L04.setText(vypln[3])
            self.L05.setText(vypln[4])
            self.L07.setText(vypln[5])
            self.L08.setText(vypln[6])
            self.L09.setText(vypln[7])
            self.L10.setText(vypln[8])
            self.L11.setText(vypln[9])
            self.L13.setText(vypln[10])
            self.L14.setText(vypln[11])
            self.L15.setText(vypln[12])
            self.L16.setText(vypln[13])
            self.L17.setText(vypln[14])
            self.L19.setText(vypln[15])
            self.L20.setText(vypln[16])
            self.L21.setText(vypln[17])
            self.L22.setText(vypln[18])
            self.L23.setText(vypln[19])
            self.L25.setText(vypln[20])
            self.L26.setText(vypln[21])
            self.L27.setText(vypln[22])
            self.L28.setText(vypln[23])
            self.L29.setText(vypln[24])
            
        elif self.VelikostMatice==2:
            shufabc=list(self.en_abc)
            random.shuffle(shufabc)
            vypln= ''.join(shufabc)
            self.rand_abc=vypln
            self.abc=self.rand_abc
            self.L01.setText(vypln[0])
            self.L02.setText(vypln[1])
            self.L03.setText(vypln[2])
            self.L04.setText(vypln[3])
            self.L05.setText(vypln[4])
            self.L07.setText(vypln[5])
            self.L08.setText(vypln[6])
            self.L09.setText(vypln[7])
            self.L10.setText(vypln[8])
            self.L11.setText(vypln[9])
            self.L13.setText(vypln[10])
            self.L14.setText(vypln[11])
            self.L15.setText(vypln[12])
            self.L16.setText(vypln[13])
            self.L17.setText(vypln[14])
            self.L19.setText(vypln[15])
            self.L20.setText(vypln[16])
            self.L21.setText(vypln[17])
            self.L22.setText(vypln[18])
            self.L23.setText(vypln[19])
            self.L25.setText(vypln[20])
            self.L26.setText(vypln[21])
            self.L27.setText(vypln[22])
            self.L28.setText(vypln[23])
            self.L29.setText(vypln[24])
            
        elif self.VelikostMatice==0:
            shufabc=list(self.adfgvx_abc)
            random.shuffle(shufabc)
            vypln= ''.join(shufabc)
            self.rand_abc=vypln         
            self.abc=self.rand_abc
            self.L01.setText(vypln[0])
            self.L02.setText(vypln[1])
            self.L03.setText(vypln[2])
            self.L04.setText(vypln[3])
            self.L05.setText(vypln[4])
            self.L06.setText(vypln[5])
            self.L07.setText(vypln[6])
            self.L08.setText(vypln[7])
            self.L09.setText(vypln[8])
            self.L10.setText(vypln[9])
            self.L11.setText(vypln[10])
            self.L12.setText(vypln[11])
            self.L13.setText(vypln[12])
            self.L14.setText(vypln[13])
            self.L15.setText(vypln[14])
            self.L16.setText(vypln[15])
            self.L17.setText(vypln[16])
            self.L18.setText(vypln[17])
            self.L19.setText(vypln[18])
            self.L20.setText(vypln[19])
            self.L21.setText(vypln[20])
            self.L22.setText(vypln[21])
            self.L23.setText(vypln[22])
            self.L24.setText(vypln[23])
            self.L25.setText(vypln[24])
            self.L26.setText(vypln[25])
            self.L27.setText(vypln[26])
            self.L28.setText(vypln[27])
            self.L29.setText(vypln[28])
            self.L30.setText(vypln[29])
            self.L31.setText(vypln[30])
            self.L32.setText(vypln[31])
            self.L33.setText(vypln[32])
            self.L34.setText(vypln[33])
            self.L35.setText(vypln[34])
            self.L36.setText(vypln[35])

    def ResetABC(self):
        self.abc=""
        self.abcVlastni=[]
        self.L01.setText("")
        self.L02.setText("")
        self.L03.setText("")
        self.L04.setText("")
        self.L05.setText("")
        self.L06.setText("")
        self.L07.setText("")
        self.L08.setText("")
        self.L09.setText("")
        self.L10.setText("")
        self.L11.setText("")
        self.L12.setText("")
        self.L13.setText("")
        self.L14.setText("")
        self.L15.setText("")
        self.L16.setText("")
        self.L17.setText("")
        self.L18.setText("")
        self.L19.setText("")
        self.L20.setText("")
        self.L21.setText("")
        self.L22.setText("")
        self.L23.setText("")
        self.L24.setText("")
        self.L25.setText("")
        self.L26.setText("")
        self.L27.setText("")
        self.L28.setText("")
        self.L29.setText("")
        self.L30.setText("")
        self.L31.setText("")
        self.L32.setText("")
        self.L33.setText("")
        self.L34.setText("")
        self.L35.setText("")
        self.L36.setText("")
        if self.VelikostMatice==0:
            self.push_0.setEnabled(True)
            self.push_1.setEnabled(True)
            self.push_2.setEnabled(True)
            self.push_3.setEnabled(True)
            self.push_4.setEnabled(True)
            self.push_5.setEnabled(True)
            self.push_6.setEnabled(True)
            self.push_7.setEnabled(True)
            self.push_8.setEnabled(True)
            self.push_9.setEnabled(True)
            self.A.setEnabled(True)
            self.B.setEnabled(True)
            self.C.setEnabled(True)
            self.D.setEnabled(True)
            self.E.setEnabled(True)
            self.F.setEnabled(True)
            self.G.setEnabled(True)
            self.H.setEnabled(True)
            self.I.setEnabled(True)
            self.J.setEnabled(True)
            self.K.setEnabled(True)
            self.L.setEnabled(True)
            self.M.setEnabled(True)
            self.N.setEnabled(True)
            self.O.setEnabled(True)
            self.P.setEnabled(True)
            self.Q.setEnabled(True)
            self.R.setEnabled(True)
            self.S.setEnabled(True)
            self.T.setEnabled(True)
            self.U.setEnabled(True)
            self.V.setEnabled(True)
            self.W.setEnabled(True)
            self.X.setEnabled(True)
            self.Y.setEnabled(True)
            self.Z.setEnabled(True)
        elif self.VelikostMatice==1:
            self.push_0.setEnabled(False)
            self.push_1.setEnabled(False)
            self.push_2.setEnabled(False)
            self.push_3.setEnabled(False)
            self.push_4.setEnabled(False)
            self.push_5.setEnabled(False)
            self.push_6.setEnabled(False)
            self.push_7.setEnabled(False)
            self.push_8.setEnabled(False)
            self.push_9.setEnabled(False)
            self.A.setEnabled(True)
            self.B.setEnabled(True)
            self.C.setEnabled(True)
            self.D.setEnabled(True)
            self.E.setEnabled(True)
            self.F.setEnabled(True)
            self.G.setEnabled(True)
            self.H.setEnabled(True)
            self.I.setEnabled(True)
            self.J.setEnabled(True)
            self.K.setEnabled(True)
            self.L.setEnabled(True)
            self.M.setEnabled(True)
            self.N.setEnabled(True)
            self.O.setEnabled(True)
            self.P.setEnabled(True)
            self.Q.setEnabled(True)
            self.R.setEnabled(True)
            self.S.setEnabled(True)
            self.T.setEnabled(True)
            self.U.setEnabled(True)
            self.V.setEnabled(True)
            self.W.setEnabled(False)
            self.X.setEnabled(True)
            self.Y.setEnabled(True)
            self.Z.setEnabled(True)
        elif self.VelikostMatice==2:
            self.push_0.setEnabled(False)
            self.push_1.setEnabled(False)
            self.push_2.setEnabled(False)
            self.push_3.setEnabled(False)
            self.push_4.setEnabled(False)
            self.push_5.setEnabled(False)
            self.push_6.setEnabled(False)
            self.push_7.setEnabled(False)
            self.push_8.setEnabled(False)
            self.push_9.setEnabled(False)
            self.A.setEnabled(True)
            self.B.setEnabled(True)
            self.C.setEnabled(True)
            self.D.setEnabled(True)
            self.E.setEnabled(True)
            self.F.setEnabled(True)
            self.G.setEnabled(True)
            self.H.setEnabled(True)
            self.I.setEnabled(True)
            self.J.setEnabled(False)
            self.K.setEnabled(True)
            self.L.setEnabled(True)
            self.M.setEnabled(True)
            self.N.setEnabled(True)
            self.O.setEnabled(True)
            self.P.setEnabled(True)
            self.Q.setEnabled(True)
            self.R.setEnabled(True)
            self.S.setEnabled(True)
            self.T.setEnabled(True)
            self.U.setEnabled(True)
            self.V.setEnabled(True)
            self.W.setEnabled(True)
            self.X.setEnabled(True)
            self.Y.setEnabled(True)
            self.Z.setEnabled(True)
  
    def DisEn(self):
        if self.VelikostMatice == 0:
                abc=len(self.abc)
                if abc < 36:
                    self.pushButton_Sifruj.setEnabled(False)
                    self.pushButton_Desifruj.setEnabled(False)
                elif abc  == 36:
                    self.pushButton_Sifruj.setEnabled(True)
                    self.pushButton_Desifruj.setEnabled(True)
        if self.VelikostMatice == 1:
                abc=len(self.abc)
                if abc < 25:
                    self.pushButton_Sifruj.setEnabled(False)
                    self.pushButton_Desifruj.setEnabled(False)
                elif abc  == 25:
                    self.pushButton_Sifruj.setEnabled(True)
                    self.pushButton_Desifruj.setEnabled(True)
        if self.VelikostMatice == 2:
                abc=len(self.abc)
                if abc < 25:
                    self.pushButton_Sifruj.setEnabled(False)
                    self.pushButton_Desifruj.setEnabled(False)
                elif abc  == 25:
                    self.pushButton_Sifruj.setEnabled(True)
                    self.pushButton_Desifruj.setEnabled(True)
            
        
    def TA(self):
        self.A.setEnabled(False)
        self.abcVlastni.append("A")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TB(self):
        self.B.setEnabled(False)
        self.abcVlastni.append("B")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TC(self):
        self.C.setEnabled(False)
        self.abcVlastni.append("C")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TD(self):
        self.D.setEnabled(False)
        self.abcVlastni.append("D")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TE(self):
        self.E.setEnabled(False)
        self.abcVlastni.append("E")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TF(self):
        self.F.setEnabled(False)
        self.abcVlastni.append("F")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TG(self):
        self.G.setEnabled(False)
        self.abcVlastni.append("G")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TH(self):
        self.H.setEnabled(False)
        self.abcVlastni.append("H")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TI(self):
        self.I.setEnabled(False)
        self.abcVlastni.append("I")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TJ(self):
        self.J.setEnabled(False)
        self.abcVlastni.append("J")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TK(self):
        self.K.setEnabled(False)
        self.abcVlastni.append("K")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TL(self):
        self.L.setEnabled(False)
        self.abcVlastni.append("L")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TM(self):
        self.M.setEnabled(False)
        self.abcVlastni.append("M")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TN(self):
        self.N.setEnabled(False)
        self.abcVlastni.append("N")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TO(self):
        self.O.setEnabled(False)
        self.abcVlastni.append("O")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TP(self):
        self.P.setEnabled(False)
        self.abcVlastni.append("P")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TQ(self):
        self.Q.setEnabled(False)
        self.abcVlastni.append("Q")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TR(self):
        self.R.setEnabled(False)
        self.abcVlastni.append("R")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TS(self):
        self.S.setEnabled(False)
        self.abcVlastni.append("S")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TT(self):
        self.T.setEnabled(False)
        self.abcVlastni.append("T")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TU(self):
        self.U.setEnabled(False)
        self.abcVlastni.append("U")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TV(self):
        self.V.setEnabled(False)
        self.abcVlastni.append("V")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TW(self):
        self.W.setEnabled(False)
        self.abcVlastni.append("W")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TX(self):
        self.X.setEnabled(False)
        self.abcVlastni.append("X")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TY(self):
        self.Y.setEnabled(False)
        self.abcVlastni.append("Y")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def TZ(self):
        self.Z.setEnabled(False)
        self.abcVlastni.append("Z")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T0(self):
        self.push_0.setEnabled(False)
        self.abcVlastni.append("0")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T1(self):
        self.push_1.setEnabled(False)
        self.abcVlastni.append("1")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T2(self):
        self.push_2.setEnabled(False)
        self.abcVlastni.append("2")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T3(self):
        self.push_3.setEnabled(False)
        self.abcVlastni.append("3")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T4(self):
        self.push_4.setEnabled(False)
        self.abcVlastni.append("4")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T5(self):
        self.push_5.setEnabled(False)
        self.abcVlastni.append("5")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T6(self):
        self.push_6.setEnabled(False)
        self.abcVlastni.append("6")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T7(self):
        self.push_7.setEnabled(False)
        self.abcVlastni.append("7")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T8(self):
        self.push_8.setEnabled(False)
        self.abcVlastni.append("8")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def T9(self):
        self.push_9.setEnabled(False)
        self.abcVlastni.append("9")
        self.abc=self.abcVlastni
        self.DisEn()
        self.VlastniABC()
    def VlastniABC(self):
        if self.VelikostMatice==0:        
            self.L01.setText(self.abcVlastni[0])
            self.L02.setText(self.abcVlastni[1])
            self.L03.setText(self.abcVlastni[2])
            self.L04.setText(self.abcVlastni[3])
            self.L05.setText(self.abcVlastni[4])
            self.L06.setText(self.abcVlastni[5])
            self.L07.setText(self.abcVlastni[6])
            self.L08.setText(self.abcVlastni[7])
            self.L09.setText(self.abcVlastni[8])
            self.L10.setText(self.abcVlastni[9])
            self.L11.setText(self.abcVlastni[10])
            self.L12.setText(self.abcVlastni[11])
            self.L13.setText(self.abcVlastni[12])
            self.L14.setText(self.abcVlastni[13])
            self.L15.setText(self.abcVlastni[14])
            self.L16.setText(self.abcVlastni[15])
            self.L17.setText(self.abcVlastni[16])
            self.L18.setText(self.abcVlastni[17])
            self.L19.setText(self.abcVlastni[18])
            self.L20.setText(self.abcVlastni[19])
            self.L21.setText(self.abcVlastni[20])
            self.L22.setText(self.abcVlastni[21])
            self.L23.setText(self.abcVlastni[22])
            self.L24.setText(self.abcVlastni[23])
            self.L25.setText(self.abcVlastni[24])
            self.L26.setText(self.abcVlastni[25])
            self.L27.setText(self.abcVlastni[26])
            self.L28.setText(self.abcVlastni[27])
            self.L29.setText(self.abcVlastni[28])
            self.L30.setText(self.abcVlastni[29])
            self.L31.setText(self.abcVlastni[30])
            self.L32.setText(self.abcVlastni[31])
            self.L33.setText(self.abcVlastni[32])
            self.L34.setText(self.abcVlastni[33])
            self.L35.setText(self.abcVlastni[34])
            self.L36.setText(self.abcVlastni[35])
            
        elif self.VelikostMatice==1:           
            self.L01.setText(self.abcVlastni[0])
            self.L02.setText(self.abcVlastni[1])
            self.L03.setText(self.abcVlastni[2])
            self.L04.setText(self.abcVlastni[3])
            self.L05.setText(self.abcVlastni[4])
            self.L07.setText(self.abcVlastni[5])
            self.L08.setText(self.abcVlastni[6])
            self.L09.setText(self.abcVlastni[7])
            self.L10.setText(self.abcVlastni[8])
            self.L11.setText(self.abcVlastni[9])
            self.L13.setText(self.abcVlastni[10])
            self.L14.setText(self.abcVlastni[11])
            self.L15.setText(self.abcVlastni[12])
            self.L16.setText(self.abcVlastni[13])
            self.L17.setText(self.abcVlastni[14])
            self.L19.setText(self.abcVlastni[15])
            self.L20.setText(self.abcVlastni[16])
            self.L21.setText(self.abcVlastni[17])
            self.L22.setText(self.abcVlastni[18])
            self.L23.setText(self.abcVlastni[19])
            self.L25.setText(self.abcVlastni[20])
            self.L26.setText(self.abcVlastni[21])
            self.L27.setText(self.abcVlastni[22])
            self.L28.setText(self.abcVlastni[23])
            self.L29.setText(self.abcVlastni[24])
            
        elif self.VelikostMatice==2:          
            self.L01.setText(self.abcVlastni[0])
            self.L02.setText(self.abcVlastni[1])
            self.L03.setText(self.abcVlastni[2])
            self.L04.setText(self.abcVlastni[3])
            self.L05.setText(self.abcVlastni[4])
            self.L07.setText(self.abcVlastni[5])
            self.L08.setText(self.abcVlastni[6])
            self.L09.setText(self.abcVlastni[7])
            self.L10.setText(self.abcVlastni[8])
            self.L11.setText(self.abcVlastni[9])
            self.L13.setText(self.abcVlastni[10])
            self.L14.setText(self.abcVlastni[11])
            self.L15.setText(self.abcVlastni[12])
            self.L16.setText(self.abcVlastni[13])
            self.L17.setText(self.abcVlastni[14])
            self.L19.setText(self.abcVlastni[15])
            self.L20.setText(self.abcVlastni[16])
            self.L21.setText(self.abcVlastni[17])
            self.L22.setText(self.abcVlastni[18])
            self.L23.setText(self.abcVlastni[19])
            self.L25.setText(self.abcVlastni[20])
            self.L26.setText(self.abcVlastni[21])
            self.L27.setText(self.abcVlastni[22])
            self.L28.setText(self.abcVlastni[23])
            self.L29.setText(self.abcVlastni[24])
                  
                    
    def UpravaKlice(self,klic):
        klic=klic[:].upper()
        klic_novy = unicodedata.normalize('NFKD', klic).encode('ASCII', 'ignore')
        klic_novy=str(klic_novy)[0:]
#Ošetření duplicitních znaků (ponechání, ale jejich číslování)
        return klic_novy
        
    def Sifruj(self,zprava):
        klic=self.text_Klic.toPlainText()
        klic=self.UpravaKlice(klic)
        zprava=self.text_Vstup.toPlainText()
        zprava = zprava[:].upper()
#Tabulka k první části šifrování zprávy 
        if self.VelikostMatice==0:
            zprava = zprava.replace(" ","MEZERA")
            zprava= ''.join(c for c in unicodedata.normalize('NFD',zprava)
                       if unicodedata.category(c) !='Mn')
            zprava=str(zprava)[0:]
            intab="ADFGVX"
            tabulka1=[[self.abc[6*i+j] for j in range(6)] for i in range(6)]
            
        if self.VelikostMatice==1:
            zprava = zprava.replace("J","I")
            zprava = unicodedata.normalize('NFKD', zprava).encode('ASCII', 'ignore')
            zprava=str(zprava)[0:]
            
            intab="ADFGX"
            tabulka1=[[self.abc[5*i+j] for j in range(5)] for i in range(5)]
            
        if self.VelikostMatice==2:
            zprava = zprava.replace("W","V")
            zprava = unicodedata.normalize('NFKD', zprava).encode('ASCII', 'ignore')
            zprava=str(zprava)[0:]
            intab="ADFGX"
            tabulka1=[[self.abc[5*i+j] for j in range(5)] for i in range(5)]

        zprava_po_prvnicasti = ''
        for x in zprava:
            i, j = 0, 0
            while True:
                if x == tabulka1[i][j]:
                    break
                j= (j+1) % len(tabulka1[i])
                if j == 0:
                    i += 1
            zprava_po_prvnicasti += intab[i] + intab[j]
            
        klic= ''.join(sorted(set(klic), key=lambda x:klic.index(x)))
        sloupec = len(klic)
        radek = (len(zprava_po_prvnicasti)-1)//sloupec +1
        tabulka2 = [[zprava_po_prvnicasti[sloupec*i+j] if sloupec*i+j < len(zprava_po_prvnicasti) else ''
             for j in range(sloupec)]
                 for i in range(radek)]
    
        klic_dle_abecedy = ''.join(sorted(klic))
        
        tabulka3 = [[rad[klic.index(klic_dle_abecedy[c])]
                        for c in range(sloupec)]
                            for rad in tabulka2]
        zprava_zasifrovana = ''.join(tabulka3[i][j]
                                        for j  in range(sloupec)
                                            for i in range(radek))
        self.textBrowser.clear()
        self.textBrowser.append("".join(zprava_zasifrovana))
        self.textBrowser.show()

    
    def Desifruj(self,zprava):
        
        klic=self.text_Klic.toPlainText()
        klic=self.UpravaKlice(klic)
        zprava=self.text_Vstup.toPlainText()
        
        klic= ''.join(sorted(set(klic), key=lambda x:klic.index(x)))
        klic_dle_abecedy = ''.join(sorted(klic))
        sloupec = len(klic)
        radek = (len(zprava)-1)//sloupec+1
        
        tabulka1 = [[""]*sloupec for x in range(radek)]
        i=0
        for sloup in range(sloupec):
            for rad in range(radek):
                sloupec2 = klic.index(klic_dle_abecedy[sloup])
                if rad * sloupec + sloupec2 >= len(zprava):
                    continue
                else:
                    tabulka1[rad][sloupec2]=zprava[i]
                    i += 1
                    
        zprava_po_prvnifazi= ''.join(''.join(rad) for rad in tabulka1)
        
        if self.VelikostMatice == 0:
            intab = "ADFGVX"
            tabulka_org=[[self.abc[6*i+j] for j in range(6)] for i in range(6)]
        if self.VelikostMatice == 1:
            intab = "ADFGX"
            tabulka_org=[[self.abc[5*i+j] for j in range(5)] for i in range(5)]
        if self.VelikostMatice == 2:
            intab = "ADFGX"
            tabulka_org=[[self.abc[5*i+j] for j in range(5)] for i in range(5)]
        
        zprava_desifrovana = ''.join(tabulka_org[intab.index(zprava_po_prvnifazi[i])]
                                                [intab.index(zprava_po_prvnifazi[i+1])]
                                    for i in range(0,len(zprava_po_prvnifazi),2) )
        
        self.textBrowser.clear()
        self.textBrowser.append("".join(zprava_desifrovana))
        self.textBrowser.show()
        return
    def CistiVstup(self):
        self.text_Vstup.clear()
        
    def CistiVystup(self):
        self.textBrowser.clear()
        
    def CistiKlic(self):
        self.text_Klic.clear()

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_Sifruj.clicked.connect(self.Sifruj)
        self.pushButton_Desifruj.clicked.connect(self.Desifruj)
        self.CZ.toggled.connect(self.VyberABC)
        self.EN.toggled.connect(self.VyberABC)
        self.random.clicked.connect(self.RandomABC)
        self.reset.clicked.connect(self.ResetABC)
        self.ADFGVX.toggled.connect(self.VyberABC)
        self.ADFGX.toggled.connect(self.VyberABC)
        self.vstup.clicked.connect(self.CistiVstup)
        self.vystup.clicked.connect(self.CistiVystup)
        self.klic.clicked.connect(self.CistiKlic)
        self.textBrowser.clear()
        self.textBrowser.show()
        
        self.A.clicked.connect(self.TA)
        self.B.clicked.connect(self.TB)
        self.C.clicked.connect(self.TC)
        self.D.clicked.connect(self.TD)
        self.E.clicked.connect(self.TE)
        self.F.clicked.connect(self.TF)
        self.G.clicked.connect(self.TG)
        self.H.clicked.connect(self.TH)
        self.I.clicked.connect(self.TI)
        self.J.clicked.connect(self.TJ)
        self.K.clicked.connect(self.TK)
        self.L.clicked.connect(self.TL)
        self.M.clicked.connect(self.TM)
        self.N.clicked.connect(self.TN)
        self.O.clicked.connect(self.TO)
        self.P.clicked.connect(self.TP)
        self.Q.clicked.connect(self.TQ)
        self.R.clicked.connect(self.TR)
        self.S.clicked.connect(self.TS)
        self.T.clicked.connect(self.TT)
        self.U.clicked.connect(self.TU)
        self.V.clicked.connect(self.TV)
        self.W.clicked.connect(self.TW)
        self.X.clicked.connect(self.TX)
        self.Y.clicked.connect(self.TY)
        self.Z.clicked.connect(self.TZ)
        self.push_0.clicked.connect(self.T0)
        self.push_1.clicked.connect(self.T1)
        self.push_2.clicked.connect(self.T2)
        self.push_3.clicked.connect(self.T3)
        self.push_4.clicked.connect(self.T4)
        self.push_5.clicked.connect(self.T5)
        self.push_6.clicked.connect(self.T6)
        self.push_7.clicked.connect(self.T7)
        self.push_8.clicked.connect(self.T8)
        self.push_9.clicked.connect(self.T9)
        
#ToolTips
        
        self.CZ.setToolTip('Will set language as Czech.') 
        self.EN.setToolTip('Will set language as English.')
        self.ADFGVX.setToolTip('Size of matrix willbe 6x6.')
        self.ADFGX.setToolTip('Size of matrix will be 5x5(pick language).') 
        self.pushButton_Sifruj.setToolTip('Click to encrypt your message.') 
        self.pushButton_Desifruj.setToolTip('Click to decrypt your message')
        self.random.setToolTip('For random matrix of picked language.')
        self.reset.setToolTip('Reset your matrix and fill out with picked language.')
        self.vstup.setToolTip('Clears the field of an input.') 
        self.vystup.setToolTip('Clears the field of an output.') 
        self.klic.setToolTip('Clears the field of a key.') 
         
if __name__ == "__main__":            
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())