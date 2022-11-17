x = input("quanti numeri vuoi inserire?")
x = int(x)
lista=[]
for y in range(x):
    z = input("inserisci numero:")
    z = int(z)
    lista.append(z*z)
print(lista)