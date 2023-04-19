#Crear un diccionario que contenga los nombres y edades de varias personas:

dicc=dict()
while True:
    getInputUserName=input('Introduce nombre: ')

    getInputUserAge=input('Introduce edad: ')

    dicc[f'{getInputUserName}']= f'{getInputUserAge}'

    finalizarPrograma=input('¿Desea finalizar el programa?(s/n): ')
    if finalizarPrograma=='s':
        print(dicc)
        break


