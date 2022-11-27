import os
import time
clear = lambda: os.system('cls')
def christmas_tree(h, c):
    n_ast = 1
    n_spc = h-1

    for i in range(0, h):
        print(n_spc * ' ' , n_ast * c)
        n_ast = n_ast +2
        n_spc = n_spc -1

#Richiedo l'input all'utente
height = int(input("Dimmi l'altezza: "))
char = input("Dimmi un carattere: ")
char2 = input("Dimmi un carattere: ")

turno = True #Uso questa variabile per alternare la stampa dei due caratteri
#Faccio lampeggiare l'albero 20 volte (10 secondi)

for i in range(0, 20):
    clear()  # Cancella la console
    if turno == True: christmas_tree(height, char)
    else: christmas_tree(height, char2)
    turno = not turno #l'operatore logico not inverte il valore di una variabile boolean s: not true => false  | not false = true
    time.sleep(0.5) #Blocca l'esecuzione di un programma per 0.5 secondi
