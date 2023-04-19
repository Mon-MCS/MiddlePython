from EjercicioComprension import ProcesoSubMenu
import EjerciciosClases
import EjerciciosJSON

def main():

        while True:
            print('EjercicioComprension')
            print('EjerciciosClases')
            print('EjerciciosJSON')
            inputUser=input('Elije que caperta desea inspeccionar: ')
            DirecctorioSeleccionado(inputUser)
            

def DirecctorioSeleccionado(parametro):
        if parametro=='EjercicioComprension':
            ejecute= ProcesoSubMenu.SubMenuCompresion()
            ejecute.main()           
        elif parametro=='EjerciciosClases':
            pass
        elif parametro=='EjerciciosJSON':
            pass
        else:
            print('Por favor, seleccione una de las opciones de las que dispone.')

main()