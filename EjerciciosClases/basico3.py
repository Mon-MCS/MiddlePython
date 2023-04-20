import json
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

def main():

    producto_lista = []
    producto1 = Producto("Leche", 2.50, 10)
    producto2 = Producto("Huevo", 1.50, 20)
    producto3 = Producto("Pan", 1.00, 15)
    producto_lista.append({"nombre":producto1.nombre, "precio":producto1.precio, "stock":producto1.stock})
    producto_lista.append({"nombre":producto2.nombre, "precio":producto2.precio, "stock":producto2.stock})
    producto_lista.append({"nombre":producto3.nombre, "precio":producto3.precio, "stock":producto3.stock})
    print(producto_lista)
    jsonProductoLista = json.dumps(producto_lista)
    print(jsonProductoLista)


if __name__=='__main__':
    main()