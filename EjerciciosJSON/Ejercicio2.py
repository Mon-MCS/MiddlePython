#Transacción financiera:

import json

JSONconversion=dict()

def main():
    
    Parametros()


def Parametros():
    inputId=input("Introduce un id: ")
    JSONconversion["id"]=inputId
    inputFechaYHora=input("Introduce fecha y hora: ")
    JSONconversion["Fecha y Hora"]= inputFechaYHora
    inputMonto=input("Introduce un monto: ")
    JSONconversion["Monto"]=inputMonto
    inputTipo=input('Introduce el tipo: ')
    JSONconversion["Tipo"]=inputTipo
    inputProducto=input('Introduce nombre, precio por separado: ').split()
    JSONconversion["Producto"]=f'["nombre:""{inputProducto[0]}", "precio:"{inputProducto[1]}]'
    inputDescripcion=input('Introduce una breve descripcion: ')
    JSONconversion["Descripcion: "]=inputDescripcion
    ConversionJSONPython(JSONconversion)


def ConversionJSONPython(parametro):
    
    #Serializamos el objeto a JSON
    dicInformacionUsuario=json.dumps(parametro)
    print(type(dicInformacionUsuario))
    print(dicInformacionUsuario)

if __name__=='__main__':
    main()