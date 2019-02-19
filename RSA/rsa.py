# -*- coding: utf-8 -*-
"""
Úkol č. 5 - Šifra RSA

@author: Michaela Frodlová


1) Generování veřejného a privátního klíče.
2) Převod textu do numerické reprezentace a zpět z numerické reprezentace na text
3) Šifrování pomocí veřejného klíče.
4) Dešifrování pomocí privátního klíče.
5) GUI:     a) Pole pro zadání textu
            b) Pole pro zadání klíče (n,d/n,e)
            c) Přepínač pro šifrování a dešifrování
            d) Pole pro zobrazení zašifrované/dešifrované zprávy
            e) Výpis klíčových párů
"""


import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui, uic
import math
import gmpy2

qtCreatorFile = "rsa.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):
    
    cesta_privKlic = ""
    cesta_pubKlic=""
    
    privKlic = [0,0]
    pubKlic = [0,0]

    
    en_de=0
        
    def Vyber(self):
        if self.en.isChecked() and self.en_de == 0:
            pass
        elif self.en.isChecked() and self.en_de == 1:
            self.en_de = 0
        elif self.de.isChecked() and self.en_de == 0:
            self.en_de=1
        else:
            pass
    def clearE(self):
        self.e.clear()
        self.e.show()
    def clearD(self):
        self.d.clear()
        self.d.show()
    def clearN(self):
        self.n.clear()
        self.n.show()
    def clearI(self):
        self.textEdit.clear()
        self.textEdit.show()
    def clearO(self):
        self.textBrowser.clear()
        self.textBrowser.show()
        
    def ExportPubKlic(self):

        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        cesta, _ = QFileDialog.getSaveFileName(self,"Zvolte místo pro uložení souboru s veřejným klíčem","Soubor s veřejným klíčem ","(*.rsa)", options=options)
        if cesta:
            self.cesta_pubKlic = cesta
            with open(self.cesta_pubKlic, "w") as file:
                for item in self.pubKlic:
                    file.write('%s\n' %item)
    
            
    def ExportPrivKlic(self):

        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        cesta, _ = QFileDialog.getSaveFileName(self,"Zvolte místo pro uložení souboru s privátním klíčem","Soubor s privátním klíčem ","(*.rsa)", options=options)
        if cesta:
            self.cesta_privKlic = cesta
            with open(self.cesta_privKlic, "w") as file:
                for item in self.privKlic:
                    file.write('%s\n' %item)

    def ImportPubKlic(self):

        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        cesta, _ = QFileDialog.getOpenFileName(self,"Zvolte soubor s veřejným klíčem","","(*.rsa)", options=options)
        if cesta:
            self.cesta_pubKlic = cesta
            with open(self.cesta_pubKlic,"r") as file:
                for line in file:
                    self.pubKlic.append(line)
            self.n.clear()
            self.n.setPlainText(self.pubKlic[0])
            self.n.show()
            self.e.clear()
            self.e.setPlainText(self.pubKlic[1])
            self.e.show()

            
    def ImportPrivKlic(self):

        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        cesta, _ = QFileDialog.getOpenFileName(self,"Zvolte soubor s privátním klíčem","","(*.rsa)", options=options)
        if cesta:
            self.cesta_privKlic = cesta
            with open(self.cesta_privKlic,"r") as file:
                for line in file:
                    self.privKlic.append(line)
            self.n.clear()
            self.n.setPlainText(self.privKlic[0])
            self.n.show()
            self.d.clear()
            self.d.setPlainText(self.privKlic[1])
            self.d.show()
        

    def generate(self):
        output = []
        with open('primerand.txt') as a:
            output = a.read().splitlines()
        p= random.choice(output)
        q= random.choice(output)
        p = int(p)
        q = int(q)
        if p == q:
            p= random.choice(output)
# n = pq
        n = p*q
# φ(n) = (p − 1)(q − 1).
        eun = (p-1)*(q-1)
# 1 < e < φ(n)
        e = random.randrange(1,eun)
# Největší společný dělitel = 1
        verif = math.gcd(e,eun)
        while verif !=1:
            e = random.randrange(1,eun)
            verif = math.gcd(e,eun)
# Inverzní modulo = e mod φ(n)
        d = gmpy2.invert(e,eun)
        
        n=str(n)
        e=str(e)
        d=str(d)
        
        self.pubKlic[0] = n
        self.pubKlic[1] = e
        self.privKlic[0] = n
        self.privKlic[1] = d
    
        self.e.clear()
        self.e.setPlainText(e)
        self.e.show()
        self.d.clear()
        self.d.setPlainText(d)
        self.d.show()
        self.n.clear()
        self.n.setPlainText(n)
        self.n.show()
        if self.cesta_pubKlic != "":
            a = open(self.cesta_pubKlic, "w")
            a.write(str(self.pub_Klic))
            a.close()
        return n,e,d
    
    def go(self):
# Šifrování   
        if self.en_de==0:
            if self.e == "" or self.n == "":
                self.textBrowser.append("Zadejte část e i část n.")
            zprava = self.textEdit.toPlainText()
            e = self.e.toPlainText()
            e = int(e)
            n = self.n.toPlainText()
            n = int(n)
            blokovy_pristup = 7
# Převod textu do ascii, následně do binárky, poté do nbit čisla a pak do dec čisla
            bloky_zprava = [zprava[i:i+blokovy_pristup] for i in range(0,len(zprava),blokovy_pristup)]            
            ascii_list=list(bloky_zprava)
            bin_list_bloky=[]
            bin_doplneno=[]
            dec=0
            Sifra_one = 0
            nbit_bloky=[]
            dec_bloky=[]
            Sifra=[]
            Sifra_str=[]
            for i in ascii_list:
                listicek = []
                for j in i:
                        listicek.append(bin(ord(j))[2:])
                bin_list_bloky.append(listicek)
            for j in bin_list_bloky:
                listicek2 = []
                for u in j:
                    listicek2.append(((10 - len(u)) * '0') + u)
                bin_doplneno.append(listicek2)
            for k in bin_doplneno:
                nbit = ""
                for i in k:
                    nbit += i
                nbit_bloky.append(nbit)
            for x in nbit_bloky:
                dec = int(x,2)
                dec_bloky.append(dec)
# c = m^e mod n
            for i in dec_bloky:
                Sifra_one = pow(i,e,n)
                Sifra.append(Sifra_one)
            for l in Sifra:
                Sifra_str.append(str(l))
            self.textBrowser.clear()
            self.textBrowser.append(" ".join(Sifra_str))
            self.textBrowser.show()
            
                            
# Dešifrování            
        elif self.en_de==1:
            Kalkulace  = 0
            kalk_fin = []
            binarka_blok = []
            blokybloku=[]
            bin_doplneno=[]
            finalni_zprava=[]
            blokyblokuopacne=[]
            bbbez0=[]
            bez_bloku=[]
            zprava=self.textEdit.toPlainText()
            d = self.d.toPlainText()
            d = int(d)
            n = self.n.toPlainText()
            n = int(n)
            zprava_list = list(map(int, zprava.split()))
            for i in zprava_list:
                Kalkulace = pow(i,d,n)
                kalk_fin.append(Kalkulace)
            for x in kalk_fin:
                binarka_blok.append(bin(x))
            for a in binarka_blok:
                bloky=[]
                while len(a):
                    bloky.append(a[-10:])
                    a = a[:-10]
                blokybloku.append(bloky)
            for p in blokybloku:
                blokyblokuopacne.append(p[::-1])
            for u in blokyblokuopacne:
                bez0b=[]
                for l  in u:
                    bez0b.append(l.replace('0b',''))
                bbbez0.append(bez0b)
            for j in bbbez0:
                bin_doplnujeme=[]
                for q in j:
                    bin_doplnujeme.append(((10 - len(q)) * '0') + q)
                bin_doplneno.append(bin_doplnujeme)
            for pismeno in bin_doplneno:
                finalni_zprava_bloky=[]
                for pismenko in pismeno:
                        finalni_zprava_bloky.append(chr(int(pismenko,2)))
                finalni_zprava.append(finalni_zprava_bloky)
            finalni_zprava_bb=[]
            for k in finalni_zprava:
                bez_bloku= ''.join(k)
                finalni_zprava_bb.append(bez_bloku)
            self.textBrowser.clear()
            self.textBrowser.append("".join(finalni_zprava_bb))
            self.textBrowser.show()    
            
 
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Button.clicked.connect(self.go)
        self.BimportPub_key.clicked.connect(self.ImportPubKlic)
        self.BimportPriv_key.clicked.connect(self.ImportPrivKlic)
        self.BexportPub_key.clicked.connect(self.ExportPubKlic)
        self.BexportPriv_key.clicked.connect(self.ExportPrivKlic)
        self.clear_n.clicked.connect(self.clearN)
        self.clear_e.clicked.connect(self.clearE)
        self.clear_d.clicked.connect(self.clearD)
        self.clear_input.clicked.connect(self.clearI)
        self.clear_output.clicked.connect(self.clearO)
        self.Generate_B.clicked.connect(self.generate)
        self.en.toggled.connect(self.Vyber)
        self.de.toggled.connect(self.Vyber)
        self.textBrowser.clear()
        self.textBrowser.show()
        
#ToolTips
        
        self.en.setToolTip('Toggle for encrypting your message.') 
        self.de.setToolTip('Toggle for decrypting your message.')
        self.Button.setToolTip('Press and the MAGIC will happen !!!')
        self.Generate_B.setToolTip('Press to generate Public and Privat key.')
        self.BimportPub_key.setToolTip('Press to import your public key.')
        self.BimportPriv_key.setToolTip('Press to import your privat key.')
        self.BexportPub_key.setToolTip('Press to save your public key.')
        self.BexportPriv_key.setToolTip('Press to save your privat key.')
        self.clear_n.setToolTip('Press and clear "n" ')
        self.clear_e.setToolTip('Press and clear "e" ')
        self.clear_d.setToolTip('Press and clear "d" ')
        self.clear_input.setToolTip('Press and clear text input. ')
        self.clear_output.setToolTip('Press and clear results. ')
        
if __name__ == "__main__":            
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())