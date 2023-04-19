'''
3. Dada la siguiente lista de productos. 
productos_lista = [
    {"nombre": "Leche", "precio": 2.50, "stock": 10},
    {"nombre": "Huevos", "precio": 1.50, "stock": 20},
    {"nombre": "Pan", "precio": 1.00, "stock": 15}
]

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.
'''
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar(self):
        print(f"nombre:{self.nombre}, precio:{self.precio}, stock:{self.stock}")
        
producto_lista = []
producto_lista.append(Producto("Leche", 2.50, 10))
producto_lista.append(Producto("Huevo", 1.50, 20))
producto_lista.append(Producto("Pan", 1.00, 15))
producto_lista[0].mostrar()
producto_lista[1].mostrar()
producto_lista[2].mostrar()