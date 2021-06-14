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
def quantileChiQuadro5gradi(alfa):
    livello = 1 - alfa
    tavola = {
            0.95 : 11.07050, 0.975 : 12.83250,
            0.99 : 15.08627, 0.995 : 16.74960
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
        frequenzeAssolute.append(int(input('frequenza del lato ' + str(i) + ': ')))
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
        print('\nE\' stato inserito un risultato non consentito in un dado a 6 facce.')
        print('Chiusura programma...')
        exit()
    return frequenzeAssolute


# controlla se np (in questo test è uguale per ogni j) è minore di 5,
# nel caso lo fosse, significa che ogni npj è < 5 e non è possibile eseguire 
# il test, perché altrimenti si avrebbe un quantile chi quadro con 0 gradi di liberta'.
# In questo caso il programma termina
#
# input:
# np (float): npj valido per ogni j -> (n * pj) con pj=1/6 per ogni j=1,...,6
#
def checkMinore5(np):
    if (np < 5):
        print('\nNumero di tentativi troppo basso.')
        print('Chiusura programma...')
        exit()


# calcola il totale delle frequenze assolute, ovvero n
#
# input:
# frequenzeAssolute (array/int): le frequenze assolute di ogni risultato del dado
#
# output:
# totaleFrequenzeAssolute (int): il totale delle frequenze assolute, ovvero n
#
def calcoloTotaleFrequenzeAssolute(frequenzeAssolute):
    totaleFrequenzeAssolute = 0
    for frequenza in frequenzeAssolute[1:7]:
        totaleFrequenzeAssolute += frequenza
    return totaleFrequenzeAssolute


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


# stampa il menu' per la scelta del livello del test
#
def menuSceltaLivelloTest():
    print('scegli il livello del test. Seleziona:')
    print('(1) : alfa = 0.05')
    print('(2) : alfa = 0.025')
    print('(3) : alfa = 0.01')
    print('(4) : alfa = 0.005')


# prende in input e controlla il livello alfa del test scelto 
# tramite un menu di selezione
# 
# output:
# alfa (float): il livello del test scelto
#
def inserisciLivelloTest():
    switch = {
        1 : 0.05,
        2 : 0.025,
        3 : 0.01,
        4 : 0.005
    }

    while(True):
        try:
            alfa = int(input('>> '))
            alfa = switch[alfa]
        except (KeyError, ValueError):
            print('Inserito un valore non consentito, riprova...')
            alfa = False
        finally:
            if (alfa):
                break
    return alfa


# controlla se il dado è truccato o meno, ovvero se ci troviamo
# in regione critica o meno nel test
#
# input:
# Do (float): 
# quantileChiQuadro (float):
#
# output:
# True (bool): se ci troviamo in regione critica e il dado è truccato
# False (bool): se l'ipotesi del dado equilibrato è accettabile 
# 
def checkDadoTruccato(Do, quantileChiQuadro):
    if (Do > quantileChiQuadro):
        return True
    return False


##########################
#          MAIN          #
##########################
if __name__ == '__main__':

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
    print(f'\nfrequenze assolute: {frequenzeAssolute[1:]}')

    # calcola n
    totaleFrequenzeAssolute = calcoloTotaleFrequenzeAssolute(frequenzeAssolute)
    print(f'totale n: {totaleFrequenzeAssolute}')
    
    # calcola gli npj che saranno tutti uguali
    np = calcoloNPj(totaleFrequenzeAssolute)

    # controlla se gli npj sono < 5
    checkMinore5(np)

    # calcola la formula D0
    Do = D0(np, frequenzeAssolute)
    print(f'D0: {Do}\n')

    # scegli il livello del test
    menuSceltaLivelloTest()
    alfa = inserisciLivelloTest()
    
    # ottieni il quantile chi quadro in base al livello del test scelto
    quantile = quantileChiQuadro5gradi(alfa)

    # controlla se il dado è truccato o potrebbe definirsi equilibrato
    if (checkDadoTruccato(Do, quantile)):
        print(f'\nD0 > {quantile} : il dado e\' truccato')
    else:
        print(f'\nD0 <= {quantile} : il dado dovrebbe essere equilibrato')
