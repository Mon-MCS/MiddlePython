#Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:
import math

# listaNumeros={'1':int(math.pow(1,2)),'2':int(math.pow(2,2)),'3':int(math.pow(3,2)),'4':int(math.pow(4,2)),'5':int(math.pow(5,2))}

# for x,y in listaNumeros.items():
#     print(f'El cuadrado de {x} es {y}')

dicc={i:i**2 for i in range(1,6)}
print(dicc)


