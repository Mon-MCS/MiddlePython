'''
1. Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) 
y `grosor` (entero). El constructor debe inicializar ambos atributos con valores 
por defecto. Agregar un método `escribir` que imprima por pantalla la frase 
"Escribiendo con un lapiz de [color] y grosor [grosor]". 
Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.
'''

class Lapiz:
    def __init__(self,color="",grosor=""):
        self.color = color
        self.grosor = grosor
    def escribir(self):
        print(f"Escribiendo con un lápiz de {self.color} y grosor {self.grosor}")

miLapiz = Lapiz()
miLapiz.escribir()
miLapiz1 = Lapiz("azul","2B")
miLapiz1.escribir()