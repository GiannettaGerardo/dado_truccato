import math
import sys


# chiede in input le frequenze di ogni risultato possibile
# in questo caso i possibili risultati sono {1, 2, 3, 4, 5, 6}
#
# output:
# frequenzeAssolute (array/int): contiene il totale dei vari risultati
#
def inputFrequenze():
    frequenzeAssolute = []
    # la posizione 0 della lista non serve
    frequenzeAssolute.append(-1)
    for i in range(1, 7):
        print(f'Frequenza del lato {i}: ')
        frequenzeAssolute.append(int(input()))
    return frequenzeAssolute


# calcola le frequenze di ogni risultato possibile in base ai singoli
# risultati inseriti come parametro di input nel programma
#
# input:
# risultatiSingoliLanci (array/string): contiene i risultati dei singoli lanci inseriti
#                                       in input all'avvio del programma
# 
# output:
# frequenzeAssolute (array/int): contiene il totale dei vari risultati
#
def calcoloSingoleFrequenze(risultatiSingoliLanci):
    frequenzeAssolute = [0] * 7
    # la posizione 0 della lista non serve
    frequenzeAssolute[0] = -1
    for risultato in risultatiSingoliLanci[1:]:
        frequenzeAssolute[int(risultato)] += 1
    return frequenzeAssolute


# calcola gli NPj, ovvero la formula n*pj per ogni j=1,..,6
#
# input:
# n (int): totale frequenze assolute
#
# output:
# np (array/float): array contenente tutti gli npj  
#
def calcoloNPj(n):
    np = []
    for j in range(6):
        np.append(n * (1/6))
    return np


# calcola la formula D0, ovvero:2
#
#     n
# Sommatoria ((nj - npj)**2)/npj
#    j=0
#
# input:
# np (array/float): contiene gli npj
# fa (array/int): contiene le frequenze assolute
#
# output:
# Do (float): la formula D0 calcolata 
#
def D0(np, fa):
    Do = 0
    # np parte da 0
    # fa parte da 1
    for j in range(6):
        Do += ((fa[j+1] - np[j])**2) / np[j]
    return Do


##########################
#          MAIN          #
##########################
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

    Do = D0(np, frequenzeAssolute)
    print(Do)

