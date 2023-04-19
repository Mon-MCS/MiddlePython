#Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por "EOI", 
# los múltiplos de 5 por "Cloud" y los múltiplos de ambos por "EOICloud".

listaNumeros=list()

listaNumeros=[i for i in range(1,21)]

for i in listaNumeros:
    int(i)
    
    if i%3==0 and i%5==0:
        listaNumeros[i-1]='EOICloud'
        continue
    elif i%3==0:
        listaNumeros[i-1]='EOI'
        continue
    elif i%5==0:
        listaNumeros[i-1]='Cloud'
        continue

print(listaNumeros)

    