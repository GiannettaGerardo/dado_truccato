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


# fa : frequenze assolute
def calcoloNPj(fa)
    np = []
    for i in range(1:7):
        npj = fa[i]*(1/6)
        subList = [npj, npj >= 5]
        np.append(subList)
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

    for frequenza in frequenzeAssolute[1:6]:
        totaleFrequenzeAssolute += frequenza
    print(totaleFrequenzeAssolute) # debug
