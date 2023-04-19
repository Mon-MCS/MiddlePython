'''
4. Dada la siguiente lista de alumnos. 
alumnos_lista = [
       {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
       {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
       {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.

La clase deberá tener un método que incorpore el promedio de las notas del alumno.
'''
class Alumnos:
    def __init__(self,nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas 
        self.media = ""
        
    def fmedia(self):
        try:
            self.media = round(sum(self.notas)/len(self.notas),2)
        except Exception as e:
            print(f"Se ha producido el siguiente error\n {e}")
    
    def mostrar(self):
        if self.media == "":
            print(f"El alumnos es {self.nombre} {self.apellido}, cuya edad es {self.edad} y sus notas son {self.notas}") 
        else:
            print(f"El alumnos es {self.nombre} {self.apellido}, cuya edad es {self.edad} y sus notas son {self.notas}, por lo que su nota media es {self.media}")        
alumnos_lista = []
alumnos_lista.append(Alumnos("Juan", "Pérez", 20, [7,8,9]))
alumnos_lista.append(Alumnos("María", "González", 22, [6,9,10]))
alumnos_lista.append(Alumnos("Pedro", "García", 21, [5,7,8]))
alumnos_lista[0].mostrar()
alumnos_lista[1].mostrar()
alumnos_lista[2].mostrar()

alumnos_lista[0].fmedia()
alumnos_lista[1].fmedia()
alumnos_lista[2].fmedia()

alumnos_lista[0].mostrar()
alumnos_lista[1].mostrar()
alumnos_lista[2].mostrar()