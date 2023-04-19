import json

def pythonJSON(info):
    # Convertir un objeto Python a JSON
    infoJSON = json.dumps(info)

    print(info, type(info))
    print(infoJSON, type(infoJSON))

    # Convertir un objeto JSON a Python
    stringJSONinfo = str(infoJSON)
    info1 = json.loads(stringJSONinfo)
    print(info1, type(info1))
    
### Programa 1: Información sobre un usuario: 
'''
El JSON generado deberá ser:
{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", 
"trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
'''

usuario = {
    "nombre":"Juan",
    "edad":30,
    "email":"juan@acme.com",
    "trabajo":{
        "empresa":"Acme Corp",
        "puesto":"Ingeniero de software"
    }
}

pythonJSON(usuario)
