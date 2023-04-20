import json
#Ejercicio hecho en clase
'''
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, 
"historial_medico": {"alergias": ["penicilina", "mariscos"], 
"problemas_cardiacos": false, 
"medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, 
"ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}
'''

def main():

    # Pedimos la información por teclado
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    alergias = input("Ingrese sus alergias separadas por coma (si no tiene, deje vacío): ")
    alergias = alergias.split(",") if alergias else []

    # if alergias:
    #    alergias = alergias.split(",")
    # else:
    #     alergias = []


    problemas_cardiacos = input("¿Tiene problemas cardiacos? (s/n): ").lower()
    if problemas_cardiacos == "s":
        problemas_cardiacos = True
    else:
        problemas_cardiacos = False

    medicamentos = []
    while True:
        medicamento_nombre = input("Ingrese el nombre del medicamento (o 'fin' para terminar): ")
        if medicamento_nombre == "fin":
            break
        medicamento_dosis = input("Ingrese la dosis del medicamento: ")
        medicamento = {
            "nombre": medicamento_nombre,
            "dosis": medicamento_dosis
        }
        medicamentos.append(medicamento)

    ultima_revision = input("Ingrese la fecha de su última revisión médica (formato YYYY-MM-DD): ")
    proximo_turno = input("Ingrese la fecha de su próximo turno médico (formato YYYY-MM-DD): ")

    # Creamos el diccionario correspondiente
    informacion = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "peso": peso,
        "altura": altura,
        "historial_medico": {
            "alergias": alergias,
            "problemas_cardiacos": problemas_cardiacos,
            "medicamentos": medicamentos
        },
        "ultima_revision": ultima_revision,
        "proximo_turno": proximo_turno
    }
    informacion = input("Entre JSON:")

    # Convertimos el diccionario a JSON
    json_informacion = json.dumps(informacion)

    # Imprimimos el JSON generado
    print(json_informacion)

if __name__=='__main__':
    main()