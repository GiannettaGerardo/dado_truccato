import sys


# calcola il livello della variabile chi quadro e restituisce 
# il quantile corrispondendo, solo per 6 gradi di liberta'
#
# input:
# alfa (float): livello del test
#
# output:
# tavola[livello] (float): il quantile corrispondente
#
def quantileChiQuadro6gradi(alfa):
    livello = 1 - alfa
    tavola = {
            0.95 : 12.59159, 0.975 : 14.44938,
            0.99 : 16.81189, 0.995 : 18.54758
    }
    return tavola[livello]


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
        frequenzeAssolute.append(int(input('Frequenza del lato ' + str(i) + ': ')))
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
    try:
        for risultato in risultatiSingoliLanci[1:]:
            frequenzeAssolute[int(risultato)] += 1
    except IndexError:
        print('E\' stato inserito un risultato non consentito in un dado a 6 facce.')
        print('Chiusura programma...')
        exit()
    return frequenzeAssolute


# calcola gli NPj, ovvero la formula n*pj per ogni j=1,..,6
#
# input:
# n (int): totale frequenze assolute
#
# output:
# np (float): contiene tutti il valore dei vari npj 
#             che in questo caso saranno tutti uguali  
#
def calcoloNPj(n):
    return n * (1/6)


# calcola la formula D0, ovvero:2
#
#     n
# Sommatoria ((nj - npj)**2)/npj
#    j=0
#
# input:
# npj (float): contiene gli npj (tutti uguali in questo caso, 
#              quindi sarà un solo valore)
# fa (array/int): contiene le frequenze assolute
#
# output:
# Do (float): la formula D0 calcolata 
#
def D0(npj, fa):
    Do = 0
    for j in range(1, 7):
        Do += ((fa[j] - npj)**2) / npj
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

    if (np < 5):
        print('numero di tentativi troppo basso')
        exit()

    Do = D0(np, frequenzeAssolute)
    print(Do) # debug

    print('inserisci livello')
    print(quantileChiQuadro6gradi(float(input()))) # debug
