from EjerciciosClases import basico1 as B1
from EjerciciosClases import basico2 as B2
from EjerciciosClases import basico3 as B3
from EjerciciosClases import basico4 as B4

class SubMenuClases():

    def __init__(self) -> None:
        pass
    def main(self):
        while True:
            print('---------Bienvenido a la carpeta de "EjerciciosClases"---------')
            print('1-Basico1')
            print('2-Basico2')
            print('3-Basico3')
            print('4-Basico4')
            print('5-Salir')
            userInput=input('¿Qué ejercicio desea ejecutar?(ponga el numero del ejercicio. ej: 1): ')
            self.EjercicioSeleccionado(userInput)
            if userInput=='5': break
    
    def EjercicioSeleccionado(self, parametro):
        int()
        if parametro=='1':
            B1.main()
        elif parametro=='2':
            B2.main()
        elif parametro=='3':
            B3.main()
        elif parametro=='4':
            B4.main()
        elif parametro=='5':
            return
        else:
            print('elije un valor del 1 al 5')
            
if __name__=='__main__':      
    ejectua = SubMenuClases()
    ejectua.main()