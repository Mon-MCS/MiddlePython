from ejerciciosJSON1 import pythonJSON

### Programa 2: Transacción financiera:
'''
El JSON generado deberá ser:
{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, 
"tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, 
"descripcion": "Un teléfono inteligente de última generación"}}
'''
transaccion = {
    "id": 123456789, 
    "fechayhora": "2023-04-18T12:30:00Z", 
    "monto": 500.25, 
    "tipo": "compra", 
    "producto": {
        "nombre": "Smartphone", 
        "precio": 450.00, 
        "descripcion": "Un teléfono inteligente de última generación"
    }
}

pythonJSON(transaccion)