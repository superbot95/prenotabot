#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver

from selenium import webdriver
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time

def chrome():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    return browser

def seleziona_giorno(day):
    #print("bla", day)
    if day == "Lunedi":
        return [0,1]
    elif day == "Martedi": 
        return [2,3]
    elif day == "Mercoledi":
        return [4,5]
    elif day == "Giovedi":
        return [6,7]
    elif day == "Venerdi":
        return [8,9]
    elif day == "Sabato":
        return [10,11]
    elif day == "Domenica":
        return [12,13]
    else:
        print("Giorno non disponibile")    
        import sys
        sys.exit()
    
def apri_pagina(aula):
    browser = chrome()
    if aula == 'FB':
        browser.get('https://agende.unipi.it/xop-afl-swa')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'PC':
        browser.get('https://agende.unipi.it/lfm-snn-wpj')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'RC':
        browser.get('https://agende.unipi.it/xow-pdb-krs')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'PN':
        browser.get('https://agende.unipi.it/pxk-vrp-qrs')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'PG':
        browser.get('https://agende.unipi.it/bno-irb-rbh')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'ET':
        browser.get('https://agende.unipi.it/gfd-try-kjq')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'PCO':
        browser.get('https://agende.unipi.it/iqq-lno-fah')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'SVO':
        browser.get('https://agende.unipi.it/krp-lrn-gbp')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    else:
        print("Aula studio non trovata")
        import sys
        sys.exit()

def trova_posto(pagina, lista):
     continua = True 
     
     while continua:
        pagina.refresh()
        while True:   
            time.sleep(3)
            button = pagina.find_elements_by_class_name('fc-time-grid-event')
            if len(button) >= max(lista):
                break 

        boolean =0
        for indice in lista:
            time.sleep(3)
            if not "ag-slot-mine" in button[indice].get_attribute("class"):
                time.sleep(3)
                button[indice].click()
                time.sleep(3)
                break 
				
            else:
                boolean=boolean+1
                
        if boolean == len(lista):
            continua = False

if __name__ == "__main__":
    import json 
    f = open('config.json',)
    data = json.load(f)
    day = data["giorno"]
    aula = data["aula"]
    giorno = day
    if(not str(type(day))=="<class 'list'>"):
        giorno = seleziona_giorno(day)
        
    pagina = apri_pagina(aula)
    
    
    while True:  
        time.sleep(5)
        button = pagina.find_elements_by_class_name('fc-time-grid-event')
        if len(button) >= max(giorno):
            break     
    
    
    trova_posto(pagina, giorno)
    
    
    
    
