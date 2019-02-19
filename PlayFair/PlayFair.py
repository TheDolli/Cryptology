# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:49:03 2018

Playfair šifra

@author: Michaela Frodlova
"""
import sys
import unicodedata
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

qtCreatorFile = "PlayFairGUI.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):

# Nastaví abecedu na CZ/EN pomocí výběru radio button
   
    en_abc = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    cz_abc = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    abc = cz_abc
    
    def Jazyk(self):
        
        if self.radioButton_CZ.isChecked() and self.abc == self.cz_abc:
            self.abc=self.cz_abc
        elif self.radioButton_EN.isChecked() and self.abc == self.cz_abc:
            self.abc = self.en_abc
        elif self.radioButton_EN.isChecked() and self.abc == self.en_abc:
            self.abc=self.en_abc
        else:
            self.abc=self.cz_abc
            
# Upraví přijmutý klíč od uživatele
# Unicode odstraní diakritiku, malá písmena, mezery, speciální znaky
# Odstraní opakující se písmena
            
    def UpravaKlice (self,klic):
        klic_novy=klic[:].upper()
        finalni_klic=[]
        if self.abc == self.cz_abc:
            klic_novy = klic_novy.replace("W","V")
        else:
            klic_novy = klic_novy.replace("J","I")
        diakritika = unicodedata.normalize('NFKD', klic_novy) 
        klic_novy = diakritika.encode('ASCII','ignore')
        klic_novy= str(klic_novy)[2:-1]
        for pismenko in klic_novy:
            if pismenko not in finalni_klic:
                finalni_klic.append(pismenko)
        return klic_novy

    
    def GenerujMatici(self,klic):
        matice=[]
        klic=self.UpravaKlice(klic)
        for i in klic:
            if i not in matice:
                matice.append(i)
        for i in self.abc:
            if i not in matice:
                matice.append(i)
        
        matice_list=[]
        for i in range(5):
            matice_list.append('')
            
        matice_list[0]=matice[0:5]
        matice_list[1]=matice[5:10]
        matice_list[2]=matice[10:15]
        matice_list[3]=matice[15:20]
        matice_list[4]=matice[20:25]
        return matice_list
    
    def UpravaZpravy(self,zprava_org):
        
        zprava = zprava_org[:].upper()
            
        if self.abc == self.cz_abc:
            zprava = zprava.replace("W","V")
        else:
            zprava = zprava.replace("J","I")    
        zprava_diakritika = unicodedata.normalize('NFKD', zprava) 
        zprava = zprava_diakritika.encode('ASCII','ignore')
        zprava = str(zprava)[2:-1]
        
# Pokud jsou dvě stejná písmena, přidá X po prvím písmenu                  
        e=0
        for i in range(len(zprava)//2):
            if zprava[e]==zprava[e+1]:
                zprava.insert(e+1,"X")
            e=e+2
# Pokud má zpráva lichý počet písmen, přidá X na konec (do poslední dvojce)             
        if len(zprava)%2==1:
            if zprava[-1] == "X":
                zprava += "Q"
            else:
                zprava += "X"
            
#Seskupení dvojic              
        x=0
        nova_zprava=[]
        for i in range(1,len(zprava)//2+1):
            nova_zprava.append(zprava[x:x+2])
            x=x+2
                
        return nova_zprava
        
    def Pozice(self,klic_matice,pismeno):
        for i in range(0, 5):
            for j in range(0,5):
                if klic_matice[i][j]==pismeno:
                    x=i
                    y=j
        return x,y
        
    def Sifruj(self):
        klic = self.textEdit_Key.toPlainText()
        zprava = self.textEdit_Cipher.toPlainText()
        zprava = self.UpravaZpravy(zprava)
        klic_matice = self.GenerujMatici(klic)
        self.label_01.setText(klic_matice[0][0])
        self.label_02.setText(klic_matice[0][1])
        self.label_03.setText(klic_matice[0][2])
        self.label_04.setText(klic_matice[0][3])
        self.label_05.setText(klic_matice[0][4])
        self.label_06.setText(klic_matice[1][0])
        self.label_07.setText(klic_matice[1][1])
        self.label_08.setText(klic_matice[1][2])
        self.label_09.setText(klic_matice[1][3])
        self.label_10.setText(klic_matice[1][4])
        self.label_11.setText(klic_matice[2][0])
        self.label_12.setText(klic_matice[2][1])
        self.label_13.setText(klic_matice[2][2])
        self.label_14.setText(klic_matice[2][3])
        self.label_15.setText(klic_matice[2][4])
        self.label_16.setText(klic_matice[3][0])
        self.label_17.setText(klic_matice[3][1])
        self.label_18.setText(klic_matice[3][2])
        self.label_19.setText(klic_matice[3][3])
        self.label_20.setText(klic_matice[3][4])
        self.label_21.setText(klic_matice[4][0])
        self.label_22.setText(klic_matice[4][1])
        self.label_23.setText(klic_matice[4][2])
        self.label_24.setText(klic_matice[4][3])
        self.label_25.setText(klic_matice[4][4])
        
        sifra=[]
        for e in zprava:
            p1,q1=self.Pozice(klic_matice,e[0])
            p2,q2=self.Pozice(klic_matice,e[1])
            if p1==p2:
                if q1==4:
                    q1=-1
                elif q2==4:
                    q2=-1
                sifra.append(klic_matice[p1][q1+1])
                sifra.append(klic_matice[p2][q2+1])
            elif q1==q2:
                if p1==4:
                    p1=-1
                elif p2==4:
                    p2=-1
                sifra.append(klic_matice[p1+1][q1])
                sifra.append(klic_matice[p2+1][q2])
            else:
                sifra.append(klic_matice[p1][q2])
                sifra.append(klic_matice[p2][q1])
        self.textBrowser.clear()
        self.textBrowser.append("".join(sifra))
        self.textBrowser.show()
    
    def Desifruj(self):
        klic=self.textEdit_Key.toPlainText()
        zprava=self.textEdit_Cipher.toPlainText()
        zprava = self.UpravaZpravy(zprava)
        klic_matice = self.GenerujMatici(klic)
        self.label_01.setText(klic_matice[0][0])
        self.label_02.setText(klic_matice[0][1])
        self.label_03.setText(klic_matice[0][2])
        self.label_04.setText(klic_matice[0][3])
        self.label_05.setText(klic_matice[0][4])
        self.label_06.setText(klic_matice[1][0])
        self.label_07.setText(klic_matice[1][1])
        self.label_08.setText(klic_matice[1][2])
        self.label_09.setText(klic_matice[1][3])
        self.label_10.setText(klic_matice[1][4])
        self.label_11.setText(klic_matice[2][0])
        self.label_12.setText(klic_matice[2][1])
        self.label_13.setText(klic_matice[2][2])
        self.label_14.setText(klic_matice[2][3])
        self.label_15.setText(klic_matice[2][4])
        self.label_16.setText(klic_matice[3][0])
        self.label_17.setText(klic_matice[3][1])
        self.label_18.setText(klic_matice[3][2])
        self.label_19.setText(klic_matice[3][3])
        self.label_20.setText(klic_matice[3][4])
        self.label_21.setText(klic_matice[4][0])
        self.label_22.setText(klic_matice[4][1])
        self.label_23.setText(klic_matice[4][2])
        self.label_24.setText(klic_matice[4][3])
        self.label_25.setText(klic_matice[4][4])
        
        plaintext=[]
        for i in zprava:
            p1,q1=self.Pozice(klic_matice,i[0])
            p2,q2=self.Pozice(klic_matice,i[1])
            if p1==p2:
                if q1==4:
                    q1=-1
                elif q2==4:
                    q2=-1
                plaintext.append(klic_matice[p1][q1-1])
                plaintext.append(klic_matice[p1][q2-1])
            elif q1==q2:
                if p1==4:
                    p1=-1
                elif p2==4:
                    p2=-1
                plaintext.append(klic_matice[p1-1][q1])
                plaintext.append(klic_matice[p2-1][q2])
            else:
                plaintext.append(klic_matice[p1][q2])
                plaintext.append(klic_matice[p2][q1])
                
            
        self.textBrowser.clear()
        self.textBrowser.append("".join(plaintext))
        self.textBrowser.show()
                
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_Sifruj.clicked.connect(self.Sifruj)
        self.radioButton_CZ.toggled.connect(self.Jazyk)
        self.radioButton_EN.toggled.connect(self.Jazyk)
        self.textBrowser.clear()
        self.textBrowser.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
