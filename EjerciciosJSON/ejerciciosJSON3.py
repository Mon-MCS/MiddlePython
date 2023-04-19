from ejerciciosJSON1 import pythonJSON

### Programa 3: Información medica de paciente:
'''
El JSON generado deberá ser:
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, 
"altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], 
"problemas_cardiacos": false, 
"medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, 
{"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", 
"proximo_turno": "2023-05-15"}
'''

paciente = {
    "nombre": "Pedro", 
    "apellido": "Pérez", 
    "edad": 45, 
    "peso": 80.5, 
    "altura": 1.75, 
    "historial_medico": {
        "alergias": ["penicilina", "mariscos"], 
        "problemas_cardiacos": False, 
        "medicamentos": [
            {"nombre": "Ibuprofeno", "dosis": "200mg"}, 
            {"nombre": "Paracetamol", "dosis": "500mg"}
            ]
        }, 
    "ultima_revision": "2022-10-01", 
    "proximo_turno": "2023-05-15"
}

pythonJSON(paciente)