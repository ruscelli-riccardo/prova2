lista=[]
for x in range(5):
    numero = input("inserire numero:")
    numero = int(numero)
    lista.append(numero)
lista_pari=[]
for n in lista:
    check = int(n/2)
    if (check*2) == n :
        lista_pari.append(n)
lista_pari.reverse()                            #devono essere fuori da for
print(lista_pari)                       