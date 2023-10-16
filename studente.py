scelta = 0 # inizializzazione delle variabili
num = 0
nome = ""
nome_aggiunto = ""
nome_cancellato = ""
nome_da_sostituire = ""
nome_aggiornato = ""
studenti = [] # inizializzazione della lista
print("Inserisci il numero degli studenti presenti nella tua classe:") # in questo modo l'utente può creare la sua classe
num = int(input()) # input del numero degli studenti
for x in range(num): # ciclo for per aggiungere gli studenti alla classe
    print("Inserisci il nome dello studente numero:", x + 1) # la x è l'indice
    nome = input() # input del nome
    studenti.append(nome) # aggiunta dello studente alla lista studenti

while scelta < 5 : # se l'utente inserisce 5 o più il programma finisce

    print("Scegli cosa fare da questo menu")
    print("1 -- Inserimento di un nuovo studente") # creazione del menu per far scegliere all'utente cosa fare
    print("2 -- Visualizzazione degli studenti")
    print("3 -- Aggiornamento dello studente")
    print("4 -- Cancella uno studente")
    print("5 -- Esci dal programma")
    scelta = int(input()) # input della scelta dell'utente

    if scelta == 1 :
        nome_aggiunto = input("Inserisci il nome che vuoi aggiungere " ) # input del nome che si vuole aggiungere
        studenti.append(nome_aggiunto) # aggiunta in coda del nome
        print(studenti) # stampa a schermo della lista degli studenti aggiornata

    elif scelta == 2 :
        print(studenti) # stampa a schermo della lista degli studenti

    elif scelta == 3 :
        print("Inserisci il nome dello studente da sostituire")
        nome_da_sostituire = input() # input del nome che si intende cambiare
        if nome_da_sostituire in studenti: # se il nome che voglio sostituire è dentro la lista studenti
            print("Inserisci il nome dello studente aggiornato")
            nome_aggiornato = input() # input del nuovo nome
            indice = studenti.index(nome_da_sostituire) # prendo la posizione all'interno di studenti del nome che devo sostituire
            studenti[indice] = nome_aggiornato # in quella posizione ci metto il nome dello studente aggiornato
            print("Il nome è stato aggiornato con successo")
        else:
            print("Nome dello studente non trovato nella lista") # questo succede se inserisco un nome che non c'è in studenti
        print(studenti) # stampa a schermo della lista degli studenti aggiornata

    elif scelta == 4 : 
        if(num != 0): # controllo che studenti non sia vuoto
            print("Inserisci il nome che vuoi cancellare:")
            nome_cancellato = input() # input del nome da cancellare
            if nome_cancellato in studenti: # controllo se il nome da cancellare inserito è nella lista studenti
                studenti.remove(nome_cancellato) # rimozione del nome dalla lista studenti
                print("Nome cancellato con successo")
            else:
                print("Nome dello studente non trovato nella lista")
            print(studenti) # stampa a schermo della lista degli studenti aggiornata

    # elif(scelta == 5):
    #  uscita dal programma 
