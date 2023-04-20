import EjercicioComprension.EjercicioAvanzado1 as EA1
import EjercicioComprension.EjercicioAvanzado2 as EA2
import EjercicioComprension.EjercicioAvanzado3 as EA3
import EjercicioComprension.EjercicioBasico1 as EB1
import EjercicioComprension.EjercicioBasico2 as EB2
import EjercicioComprension.EjercicioBasico3 as EB3
import EjercicioComprension.EjercicioClase as EC

class SubMenuCompresion():

    def __init__(self) -> None:
        pass
    def main(self):
        while True:
            print('---------Bienvenido a la carpeta de "EjercicioCompresion"---------')
            print('1-EjercicioAvanzado1')
            print('2-EjercicioAvanzado2')
            print('3-EjercicioAvanzado3')
            print('4-EjercicioBasico1')
            print('5-EjercicioBasico2')
            print('6-EjercicioBasico3')
            print('7-EjercicioClase(Ana y Luis)')
            print('8-Salir')
            userInput=input('¿Qué ejercicio desea ejecutar?(ponga el numero del ejercicio. ej: 1): ')
            self.EjercicioSeleccionado(userInput)
            if userInput=='8': break
    
    def EjercicioSeleccionado(self, parametro):
        int()
        if parametro=='1':
            EA1.main()
        elif parametro=='2':
            EA2.main()
        elif parametro=='3':
            EA3.main()
        elif parametro=='4':
            EB1.main()
        elif parametro=='5':
            EB2.main()
        elif parametro=='6':
            EB3.main()
        elif parametro=='7':
            EC.main()
        elif parametro=='8':
            return
        else:
            print('elije un valor del 1 al 8')
            
if __name__=='__main__':      
    ejectua = SubMenuCompresion()
    ejectua.main()