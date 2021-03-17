# prenotabot


Per scaricare il programma premere sul pulsante verde "Code" e fare il Download dello ZIP

ISTRUZIONI PER INSTALLARE SU WINDOWS 10: 

Estrarre in una cartella il file ZIP scaricato

I) SETUP del giorno e dell'aula studio_

1) Aprite la cartella dove avete estratto lo ZIP

2) Aprite il file :"config.json" con un editor di testo (es. blocco note, Notepad ecc..)
 
Vi troverete scritto ad esempio: 

	{
   	 "giorno": "Lunedi",     ---> Qui va inserito il giorno o gli indici
 	   "aula": "FB"		 ---> Qui va inserita l'aula studio
	}

*__SCEGLIERE L'AULA STUDIO_
Per cambiare l'aula studio dove prenotare gli slot basta digitare il codice dell' aula tra le virgolette indicate sopra;

Codici aule: 

	'PC'	Pacinotti
	'FB'	Fibonacci
	'RC'	Ricci
	'PN'	Porta Nuova
	'PG'	Piagge

Es. Voglio prenotare al Pacinotti il Lunedì:


	{
   	 "giorno": "Lunedi",     
 	   "aula": "PC"		 
	}


*__PRENOTARE DUE SLOT LO STESSO GIORNO_
Se volete prenotare entrambi gli slot di uno stesso giorno basterà inserire il nome del giorno SENZA ACCENTI dove indicato (in questo caso è inserito il Lunedi)

*__PRENOTARE UNO SLOT OPPURE PIù SLOT IN DUE GIORNI DIVERSI_
Per prenotare un solo slot o più di uno slot ma in giorni diversi bisogna inserire invece che il nome del giorno l'indice corrispondente allo slot:

 Gli indici per gli slot sono:
          
        0	lunedì  am
        1     	   "     pm

        2	martedì am
        3  	   "    pm 

      	4	mercoledì am
        5   	   "      pm

      	6	giovedì am
        7   	   "    pm

      	8	venerdì am
        9    	   "    pm

      	10	sabato  am
        11     	   "    pm

      	12	domenica am
        13    	   "     pm

Es. Voglio prenotare UN posto lunedì pomeriggio al fibonacci: 

    {
   	 "giorno": [1],     
 	   "aula": "FB"		 
	}


Es. Voglio prenotare DUE posti alle Piagge, uno il martedì mattina e l'altro il mercoledì pomeriggio:

    {
   	 "giorno": [2,5],     
 	   "aula": "PG"		 
	}


Es. Voglio prenotare TRE posti, due il giovedì e uno il venerdì mattina al Ricci:

     {
   	 "giorno": [6,7,8],     
 	   "aula": "RC"		 
	}


II) AVVIARE PRENOTABOT

Una volta completato il SETUP potete lanciare il bot

1) Andate di nuovo nella cartella dove avete estratto lo ZIP ed installato prenotabot.exe

2) Avviate l'applicazione "prenotabot.exe" 

Inserite le vostre credenziali di ateneo ed è fatta! Da qui il bot farà tutto da solo e voi potrete pensare a tutt'altro mentre lui vi trova i posti che cercate!

!! N.B. Il computer NON DEVE ANDARE IN STANDBY fintanto che il programma è in esecuzione.


ISTRUZIONI PER Mac:

0)Si scarichino le librerie python selenium e WebDriver aprendo un terminale e digitare
	
	pip install selenium
	
	pip install webdriver-manager
	
1) Salvare in una cartella prenotapy.py


2) Aprire Qt-console/Spider/quello che preferite, entrare nella cartella dove si trova il 
   file e lanciarlo


3) Caricare la pagina delle prenotazioni dell'aula studio che preferisci scrivendo:

	aulastudio = apri_pagina(aula_studio)

  i codici sono:
	
	'PC'	Pacinotti
	'FB'	Fibonacci
	'RC'	Ricci
	'PN'	Porta Nuova
	'PG'	Piagge

  Esempio. Per aprire la pagina delle prenotazioni del Pacinotti scrivo:

	pacinotti = apri_pagina('PC') 


4) Inserire le proprie credenziali di ateneo nella pagina aperta


A questo punto si può scegliere una delle seguenti:

a) Per prenotare alla mattina: scrivere 

	prenota_mattina(aulastudio, giorno)

  I codici per giorno sono:

	0	lunedì
	2	martedì
	4	mercoledì
	6	giovedì
	8	venerdì
	10	sabato
	12	domenica

   Esempio (continuazione). Voglio prenotare giovedì al Pacinotti, scrivo:

	prenota_mattina(pacinotti, 6)

   Questa routine va fatta partire la sera prima (o quanto meno prima delle 8:30) e NON 
   bisogna fare andare in stan-by il computer.

b) Questa routine prenota un posto quando si libera. 

	trova_posto(aulastudio, giorno, slot)

   I codici per giorno sono quelli di sopra, slot può essere 0 oppure 1 a seconda che si 
   cerchi un posto la mattina o il pomeriggio rispettivamente.

   Esempio (continuazione). Voglio trovare un posto giovedì pomeriggio al pacinotti, scrivo:

	 trova_posto(pacinotti, 6, 1)

	
