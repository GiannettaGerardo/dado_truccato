import math
import sys


def inputFrequenze():
    frequenze = []
    # la posizione 0 della lista non serve
    frequenze.append(-1)
    for i in range(1, 7):
        print(f'Frequenza del lato {i}: ')
        frequenze.append(int(input()))
    return frequenze


def calcoloSingoleFrequenze(risultatiSingoliLanci):
    frequenze = [0] * 7
    # la posizione 0 della lista non serve
    frequenze[0] = -1
    for risultato in risultatiSingoliLanci[1:]:
        frequenze[int(risultato)] += 1
    return frequenze



if __name__ == '__main__':

    totaleFrequenze = 0

    if (len(sys.argv) == 1):
        frequenze = inputFrequenze()
    else:
        frequenze = calcoloSingoleFrequenze(sys.argv)
        print(frequenze)

    for frequenza in frequenze[1:6]:
        totaleFrequenze += frequenza
    print(totaleFrequenze)
