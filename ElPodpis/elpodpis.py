# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 19:55:09 2019

Úkol č. 6 - Elektronický podpis

@author: Michaela Frodlová

1) Načtení souboru pro podepsání a zobrazení základních informací (název, cesta, datum vytvoření, typ, apod.)
2) Vygenerování klíčů a podepsání souboru pomocí SHA-256 a RSA
3) Ověření dokumentu na základě elektronického podpisu
4) Manipulace se soubory s klíčí a el. podpisem (načítání a ukládání souborů s příponami .priv, .pub a .sign (.zip))
5) GUI (plně interaktivní s tlačítky pro načítání/ukládání souborů, zobrazení potřebných informací)
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui, uic
import hashlib
import sys
import random
import math
import os.path, time
from os.path import basename
import zipfile
import pathlib
import base64
import gmpy2
import shutil

qtCreatorFile = "elpodpis.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):
      
    
    cesta_souboru_nacteni=""
    cesta_souboru_ulozeni=""
    cesta_pubKlic=""
    cesta_privKlic=""
    pubKlic = [0,0]
    privKlic = [0,0]
    Podpis_str=[]
    PodpisBase64=[]
    cesta_PodpisBase64=""
    
    
    """ 
    Funkce pro generování klíčů.
    1)Random číslo z primerand.txt
    2)Výpočet n,e,d
    3)Uložení n,e,d do self.pubKlic a self.privKlic, připraveno pro export
        
    """  
    
    def Generuj(self):
        output = []
        with open('primerand.txt') as a:
            output = a.read().splitlines()
            
        p= random.choice(output)
        q= random.choice(output)
        p = int(p)
        q = int(q)
        
        if p == q:
            p= random.choice(output)
            
        n = p*q
        
        eun = (p-1)*(q-1)
        
        e = random.randrange(1,eun)
        
        verif = math.gcd(e,eun)
        while verif !=1:
            e = random.randrange(1,eun)
            verif = math.gcd(e,eun)
            
        d = gmpy2.invert(e,eun)
        
        self.pubKlic[0] = base64.standard_b64encode(str(n).encode())
        self.pubKlic[1] = base64.standard_b64encode(str(e).encode())
        print(self.pubKlic)
        self.privKlic[0] = base64.standard_b64encode(str(n).encode())
        self.privKlic[1] = base64.standard_b64encode(str(d).encode())
        print(self.privKlic)
        self.label_SavePriv.setText("<font color='green'>Ready</font>")
        self.label_SavePub.setText("<font color='green'>Ready</font>")
        return n,e,d
   
    """ 
    Načítání soukromého klíče (filedialog) a výpis informací o souboru klíče.
 
    """  
    def NactiPriv(self):
        options = QFileDialog.Options()
        cesta, _ = QFileDialog.getOpenFileName(self,"Zvolte soubor s privátním klíčem","","(*.priv)", options=options)
        if cesta:
            self.privKlic.clear()
            self.cesta_privKlic = cesta
            with open(self.cesta_privKlic,"r") as file:
                for line in file:
                    self.privKlic.append(line)
            self.label_LoadPriv.setText("<font color='green'>Loaded</font>")
            self.cesta_souboru = cesta
            self.FileName.setText(os.path.basename(self.cesta_souboru))
            self.FilePath.setText(self.cesta_souboru)
            self.Type.setText(pathlib.Path(self.cesta_souboru).suffix)
            self.FileSize.setText(str(os.path.getsize(self.cesta_souboru)))
            self.Created.setText(time.ctime(os.path.getctime(self.cesta_souboru)))
            self.LastChangeOn.setText(time.ctime(os.path.getmtime(self.cesta_souboru)))
            
    """ 
    Načítání veřejného klíče (filedialog) a výpis informací o souboru klíče.
 
    """  
    def NactiPub(self):
        options = QFileDialog.Options()
        cesta, _ = QFileDialog.getOpenFileName(self,"Zvolte soubor s veřejným klíčem",""," (*.pub)", options=options)
        if cesta:
            self.pubKlic.clear()
            self.cesta_pubKlic = cesta
            with open(self.cesta_pubKlic, "r") as file:
                for line in file:
                    self.pubKlic.append(line)
            self.label_LoadPub.setText("<font color='green'>Loaded</font>")
            self.cesta_souboru = cesta
            self.FileName.setText(os.path.basename(self.cesta_souboru))
            self.FilePath.setText(self.cesta_souboru)
            self.Type.setText(pathlib.Path(self.cesta_souboru).suffix)
            self.FileSize.setText(str(os.path.getsize(self.cesta_souboru)))
            self.Created.setText(time.ctime(os.path.getmtime(self.cesta_souboru)))
            self.LastChangeOn.setText(time.ctime(os.path.getctime(self.cesta_souboru)))
            
    """ 
    Uložení veřejného klíče (filedialog).
 
    """  
            
    def UlozPub(self):
        options = QFileDialog.Options()
        cesta, _ = QFileDialog.getSaveFileName(self,"Zvolte místo pro uložení souboru s veřejným klíčem","Soubor s veřejným klíčem ","(*.pub)", options=options)
        if cesta:
            self.cesta_pubKlic = cesta
            with open(self.cesta_pubKlic, "w") as file:
                for item in self.pubKlic:
                    file.write("%s\n" % item)
    
    """ 
    Uložení soukromého klíče (filedialog).
 
    """
    
    def UlozPriv(self):
        
        options = QFileDialog.Options()
        cesta, _ = QFileDialog.getSaveFileName(self,"Zvolte místo pro uložení souboru s privátním klíčem","Soubor s privátním klíčem ","(*.priv)", options=options)
        if cesta:
            self.cesta_privKlic = cesta
            with open(self.cesta_privKlic, "w") as file:
                for item in self.privKlic:
                    file.write("%s\n" % item)


    """ 
    Načtení souboru pro podpis/ověření a zobrazení informací o souboru.
 
    """
    def NactiSoubor(self):
        if self.SignFile.isChecked():
            options = QFileDialog.Options()
            cesta, _= QFileDialog.getOpenFileName(self,"Zvolte soubor ", "","", options=options)
            if cesta:
                self.cesta_souboru_nacteni = cesta
                self.FileName.setText(os.path.basename(self.cesta_souboru_nacteni))
                self.FilePath.setText(self.cesta_souboru_nacteni)
                self.Type.setText(pathlib.Path(self.cesta_souboru_nacteni).suffix)
                self.FileSize.setText(str(os.path.getsize(self.cesta_souboru_nacteni)))
                self.Created.setText(time.ctime(os.path.getmtime(self.cesta_souboru_nacteni)))
                self.LastChangeOn.setText(time.ctime(os.path.getctime(self.cesta_souboru_nacteni)))
                self.result.setText("File is ready." )
                
        if self.VerifyFile.isChecked():
            options = QFileDialog.Options()
            cesta, _= QFileDialog.getOpenFileName(self,"Zvolte soubor ", "","(*.zip)", options=options)
            if cesta:
                self.cesta_souboru_nacteni = cesta
                self.FileName.setText(os.path.basename(self.cesta_souboru_nacteni))
                self.FilePath.setText(self.cesta_souboru_nacteni)
                self.Type.setText(pathlib.Path(self.cesta_souboru_nacteni).suffix)
                self.FileSize.setText(str(os.path.getsize(self.cesta_souboru_nacteni)))
                self.Created.setText(time.ctime(os.path.getctime(self.cesta_souboru_nacteni)))
                self.LastChangeOn.setText(time.ctime(os.path.getmtime(self.cesta_souboru_nacteni)))
                self.result.setText("File is ready." )

        
    """ 
    Uložení již podepsaného souboru v zip.
 
    """
    def UlozSoubor(self):
        options = QFileDialog.Options()
        cesta, _= QFileDialog.getSaveFileName(self,"Zvolte soubor k podepsání", "","(*.zip)", options=options)
        if cesta:
            self.cesta_souboru_ulozeni = cesta
            
            with zipfile.ZipFile(self.cesta_souboru_ulozeni, 'w') as myzip:
                myzip.write("")
            with zipfile.ZipFile(self.cesta_souboru_ulozeni, 'a') as myzip:
                myzip.write("tempFile.sign")
            os.remove('tempFile.sign')
            os.remove(self.cesta_souboru_nacteni.split('/')[-1])

    """ 
    Funkce podpisu:
        1)SHA256
        2)RSA
        3)Base64
        4)Uložení podpisu spolu s kopií původního souboru.
 
    """          
    def Podpis(self):

        if self.SignFile.isChecked():

            h = hashlib.sha256()
            b = bytearray(128*1024)
            mv = memoryview(b)
            proRSA = ""
            with open(self.cesta_souboru_nacteni, 'rb', buffering=0) as file:
                for i in iter(lambda : file.readinto(mv), 0):
                    h.update(mv[:i])
                proRSA = h.hexdigest()
            print("proRSA", proRSA)
        
            print()
            if self.privKlic[0] == "" or self.privKlic[1] == "":
                self.result.setText("Načtěte klíč!")
            zprava = proRSA
            e = int(base64.standard_b64decode(self.privKlic[1]))
            n = int(base64.standard_b64decode(self.privKlic[0]))
            blokovy_pristup = 7

            bloky_zprava = [zprava[i:i+blokovy_pristup] for i in range(0,len(zprava),blokovy_pristup)] 
            ascii_list=list(bloky_zprava)
            bin_list_bloky=[]
            bin_doplneno=[]
            dec=0
            Sifra_one = 0
            nbit_bloky=[]
            dec_bloky=[]
            Sifra=[]
            
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

            for i in dec_bloky:
                Sifra_one = pow(i,e,n)
                Sifra.append(Sifra_one)
                
            self.PodpisBase64.clear()
            self.Podpis_str.clear()
            
            for l in Sifra:
                self.Podpis_str.append(str(l))
                
            u=','.join(self.Podpis_str)
            self.PodpisBase64.append(base64.standard_b64encode(u.encode()))
            print(self.PodpisBase64)
            self.result.setText("<font color='green'>El.Sign has been created. Press 'Save File' to save your file with el.sign. </font>" )
            shutil.copyfile(self.cesta_souboru_nacteni,self.cesta_souboru_nacteni.split('/')[:-1] )
            with open("tempFile.sign" ,"w") as file:
                file.write("RSA_SHA256 ")
                for item in self.PodpisBase64:
                    file.write(str(item)[2:-1])
                    
        if self.VerifyFile.isChecked():
            
# Dekodovani el podpisu z base 64
# Dekodovani RSA na prvotni Hash
            
            
            k = hashlib.sha256()
            l = bytearray(128*1024)
            vm = memoryview(l)
            porovnani = ""
            with open(self.cesta_souboru_nacteni, 'rb', buffering=0) as file:
                for i in iter(lambda : file.readinto(mv), 0):
                    k.update(vm[:i])
                porovnani = k.hexdigest()
                
# Porovnani hashu
    
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.SavePriv.clicked.connect(self.UlozPriv)
        self.SavePub.clicked.connect(self.UlozPub)
        self.QLoad_File.clicked.connect(self.NactiSoubor)
        self.QSave_File.clicked.connect(self.UlozSoubor)
        self.Go.clicked.connect(self.Podpis)
        self.Generate.clicked.connect(self.Generuj)
        self.LoadPriv.clicked.connect(self.NactiPriv)
        self.LoadPub.clicked.connect(self.NactiPub)
        
#Tool tips        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

