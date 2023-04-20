from SubMenuCompresion import SubMenuCompresion
from SubMenuClases import SubMenuClases
from SubMenuJSON import SubMenuJSON

def main():

        while True:
            print('EjercicioComprension')
            print('EjerciciosClases')
            print('EjerciciosJSON')
            print('Salir')
            inputUser=input('Elije que caperta desea inspeccionar: ')
            DirecctorioSeleccionado(inputUser)
            if inputUser=='Salir':
                break
            

def DirecctorioSeleccionado(parametro):
        if parametro=='EjercicioComprension':
            ejecute= SubMenuCompresion()
            ejecute.main()           
        elif parametro=='EjerciciosClases':
            ejecute1= SubMenuClases()
            ejecute1.main()
        elif parametro=='EjerciciosJSON':
            ejecute2= SubMenuJSON()
            ejecute2.main()
        elif parametro=='Salir':
            return
        else:
            print('Por favor, seleccione una de las opciones de las que dispone.')

main()