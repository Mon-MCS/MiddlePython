#Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.

listaPalabras=list()

dicc=dict()

getInputUser=input('Introduce palabras con espacios: ').split()

dicc = {i:getInputUser.count(i) for i in getInputUser}

print(dicc)

