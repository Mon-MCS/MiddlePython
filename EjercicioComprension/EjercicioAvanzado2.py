#Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.

def main():

    while True:

        listaPalabras=list()

        dicc=dict()

        getInputUser=input('Introduce palabras con espacios: ').split()


        finish=input('¿Desea finalizar(s/n): ')
        if finish=='s':
            dicc = {i:getInputUser.count(i) for i in getInputUser}
            print(dicc)
            break


if __name__=='__main__':
    main()

