#Información sobre un usuario: 
import json
JSONconversion=list()

def main():
    Parametros()

def Parametros():
    inputNombre=input("Introduce un nombre: ")
    JSONconversion.append(f"nombre: {inputNombre}")
    inputEdad=input("Introduce un edad: ")
    JSONconversion.append("edad:"+inputEdad)
    inputEmail=input("Introduce un email: ")
    JSONconversion.append(f"email: {inputEmail}")
    inputEmpresa=input("Introduce tu empresa: ")   
    inputPuesto=input("Introduce tu puesto: ")
    JSONconversion.append(f"Trabajo:[{inputEmpresa}, {inputPuesto}]")

    ConversionJSONPython(JSONconversion)


def ConversionJSONPython(parametro):
    
    #Serializamos el objeto a JSON
    dicInformacionUsuario=json.dumps(parametro)
    print(type(dicInformacionUsuario))
    print(dicInformacionUsuario)
    #Pasamos el JSON a un objeto en Python
    # dicInformacionUsuarioObj= json.loads(dicInformacionUsuario)
    # print(type(dicInformacionUsuarioObj))
    # print(dicInformacionUsuarioObj)

if __name__=='__main__':
    main()