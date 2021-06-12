import math
import sys


def inputFrequenze():
    frequenzeAssolute = []
    # la posizione 0 della lista non serve
    frequenzeAssolute.append(-1)
    for i in range(1, 7):
        print(f'Frequenza del lato {i}: ')
        frequenzeAssolute.append(int(input()))
    return frequenzeAssolute


def calcoloSingoleFrequenze(risultatiSingoliLanci):
    frequenzeAssolute = [0] * 7
    # la posizione 0 della lista non serve
    frequenzeAssolute[0] = -1
    for risultato in risultatiSingoliLanci[1:]:
        frequenzeAssolute[int(risultato)] += 1
    return frequenzeAssolute


# n : totale frequenze assolute
def calcoloNPj(n):
    np = []
    for i in range(6):
        np.append(n * (1/6))
    return np


# MAIN
if __name__ == '__main__':

    totaleFrequenzeAssolute = 0
    frequenzeAssolute = 0
    
    # esamina la scelta iniziale dell'utente:
    #   1. se l'utente non inserisce alcun risultato come parametro iniziale
    #      allora inserirà in input le frequenze di ogni risultato del dado
    #
    #   2. se l'utente inserisce i singoli risultati dei lanci del dado come parametro
    #      iniziale allora provedderà il programma a raggruppare e contare le frequenze

    if (len(sys.argv) == 1):
        frequenzeAssolute = inputFrequenze()
    else:
        frequenzeAssolute = calcoloSingoleFrequenze(sys.argv)
    
    print(frequenzeAssolute) # debug

    for frequenza in frequenzeAssolute[1:7]:
        totaleFrequenzeAssolute += frequenza
    print(totaleFrequenzeAssolute) # debug
    
    np = calcoloNPj(totaleFrequenzeAssolute)
    print(np) # debug

    if (np[0] < 5):
        print('numero di tentativi troppo basso')
        exit()

