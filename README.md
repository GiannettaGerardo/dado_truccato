# dado_truccato
Analizza i risultati di un dado a 6 facce e scopri se è truccato o meno attraverso un test del chi quadro di adattamento

## Consigli per l'utilizzo:
Il numero di tentativi da registrare deve essere adeguato (**ovvero alto**), più tentativi si inseriscono e più è affidabile il test.
## Si suggerisce un numero di tentativi >= 100 per un test più accurato
***
## Utilizzo:

### È obbligatorio inserire un numero di tentativi >= 30, altrimenti il programma terminerà con un avviso di questo tipo.

**(Procedura suggerita)** Se il programma viene avviato senza parametri di input:
```
$ python3 dado_truccato.py 
```
verrà chiesto di inserire le frequenze dei singoli risultati.
ad esempio: quante volte hai ottenuto la faccia 1 del dado, la faccia 2 del dado e così via.

Altrimenti il programma può essere avviato inserendo come parametro di input i singoli risultati dei singoli tentativi.
ad esempio: 
```
$ python3 dado_truccato.py 6 2 4 3 3 3 2 1 6 5 4 5 5 3 5 2 2 1 5 6 2 6 2 1 5 
```
**In questo caso però si faccia attenzione ad inserire un numero di risultati adeguato, perché con pochi risultati inseriti il programma non è in grado di funzionare**
