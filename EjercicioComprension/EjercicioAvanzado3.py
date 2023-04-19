#Dado un texto con una lista de ciudades con su emblema mas importante, 
# pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. 
# Nota el diccionario deberá ordenarse por su clave.
ciudadesOrdenadas={ 
    "Ámsterdam": "Los molinos de viento",
    "Buenos Aires": "El Obelisco",
    "Johannesburgo": "El león",
    "Londres": "El Big Ben",
    "Moscú": "El Kremlin",
    "Nueva York": "La Estatua de la Libertad",
    "París": "La Torre Eiffel",
    "Sídney": "La Opera de Sídney",
    "Tokio": "La flor del cerezo",
    "Dubai": "El Burj Khalifa"
}
#while True:
#    ciudad=input("Ciudad:")
#    emblema=input("Emblema")
#    ciudadesOrdenadas[ciudad]=emblema
filtro=input("Por que desea filtrar el emblema")
ciudadConFiltro = {}
for ciudad,emblema in ciudadesOrdenadas.items():
    if emblema.startswith(filtro):
        ciudadConFiltro[ciudad]=emblema

ciudadConFiltro1 = {ciudad:emblema  for ciudad,emblema in ciudadesOrdenadas.items() if emblema.startswith(filtro)}
print(f"Ciudades cuyo emblema empieza con {filtro} son:")
print(ciudadConFiltro)
print(ciudadConFiltro1)