#Crear una lista que contenga las letras de una palabra, cada una en mayúscula:

listaLetrasMayus=list()
while True:
    
    _getInputUser=input("Introduce una palabra que contenga alguna mayuscula: ")
    try:
        if _getInputUser.isnumeric():
            print('No se permiten numeros enteros y/o decimales.')
        else:
            listaLetrasMayus.append(_getInputUser)
            cantidadLetrasMayusculas=[x for x in listaLetrasMayus if x.isupper()]
            _finalizarPrograma= input('¿Desea finalizar el programa?(s/n): ')
            if _finalizarPrograma=='s':
                print(f'Estas son las letras mayusculas que ha recogido el programa: {cantidadLetrasMayusculas}')
                break

    except:  
        print('Error en la lectura del usuario.')
    
        



