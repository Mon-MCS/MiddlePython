from EjerciciosJSON import Ejercicio1 as EJSON1
from EjerciciosJSON import Ejercicio2 as EJSON2
from EjerciciosJSON import Ejercicio3 as EJSON3

class SubMenuJSON():

    def __init__(self) -> None:
        pass
    def main(self):
        while True:
            print('---------Bienvenido a la carpeta de "EjerciciosJSON"---------')
            print('1-Ejercicio1')
            print('2-Ejercicio2')
            print('3-Ejercicio3')
            print('4-Salir')
            userInput=input('¿Qué ejercicio desea ejecutar?(ponga el numero del ejercicio. ej: 1): ')
            self.EjercicioSeleccionado(userInput)
            if userInput=='4': break
    
    def EjercicioSeleccionado(self, parametro):
        int()
        if parametro=='1':
            EJSON1.main()
        elif parametro=='2':
            EJSON2.main()
        elif parametro=='3':
            EJSON3.main()
        elif parametro=='4':
            return
        else:
            print('elije un valor del 1 al 4')
            
if __name__=='__main__':      
    ejectua = SubMenuJSON()
    ejectua.main()