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

def main():

    alumnos_lista = []
    alumno1 = Alumnos("Juan", "Pérez", 20, [7,8,9])
    alumno2 = Alumnos("María", "González", 22, [6,9,10])
    alumno3 = Alumnos("Pedro", "García", 21, [5,7,8])
    alumno1.fmedia()
    alumno2.fmedia()
    alumno3.fmedia()

    alumnos_lista.append({"nombre":alumno1.nombre, "apellido":alumno1.apellido, "edad":alumno1.edad, "notas":alumno1.notas, "media":alumno1.media})
    alumnos_lista.append({"nombre":alumno2.nombre, "apellido":alumno2.apellido, "edad":alumno2.edad, "notas":alumno2.notas, "media":alumno2.media})
    alumnos_lista.append({"nombre":alumno3.nombre, "apellido":alumno3.apellido, "edad":alumno3.edad, "notas":alumno3.notas, "media":alumno3.media})
    print(alumnos_lista)

if __name__=='__main__':
    main()
