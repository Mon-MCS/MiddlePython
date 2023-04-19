#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase. 
# La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos 
# y los valores son tuplas con las sesiones a las que asistieron.

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
conjuntoAsistenciaAna=tuple(asistencias['Ana'])
conjuntoAsistenciaLuis=tuple(asistencias['Luis'])
conjuntoTotalAsistencias=(conjuntoAsistenciaAna + conjuntoAsistenciaLuis)


# 1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
print(f"El total de asistencias de ambos alumnos es {len(conjuntoTotalAsistencias)}")
print("---------------------------------------------------------")
#2. Mostrar las sesiones a las que asistieron ambos alumnos.
asistieronAmbos={x for x in conjuntoTotalAsistencias if conjuntoTotalAsistencias.count(x)==2}
# asistierionAmbos1=set()
# for x in conjuntoTotalAsistencias:
#     if conjuntoTotalAsistencias.count(x)==2:
#         asistierionAmbos1.add(x)
# print(asistierionAmbos1)
for i in asistieronAmbos:
    print(f"Ana y Luis coincidieron en la sesion {i}")       
print("---------------------------------------------------------")
#3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
noasistierionAmbos={i for i in conjuntoTotalAsistencias if conjuntoTotalAsistencias.count(i)!=2}
for e in noasistierionAmbos:
    if(conjuntoAsistenciaAna.count(e)==1):
        print(f"Ana no coincidio en la sesion {e} con Luis.")
    elif (conjuntoAsistenciaLuis.count(e)==1):
        print(f"Luis no coincidio en la sesion {e} con Ana.")
print("---------------------------------------------------------")
#4. Mostrar las sesiones a las que asistió Ana pero no Luis.
for e in noasistierionAmbos:
    if(conjuntoAsistenciaAna.count(e)==1):
        print(f"Ana no coincidio en la sesion {e} con Luis.")
print("---------------------------------------------------------")
#5. Mostrar las sesiones a las que asistió Luis pero no Ana.
for e in noasistierionAmbos:
    if (conjuntoAsistenciaLuis.count(e)==1):
        print(f"Luis no coincidio en la sesion {e} con Ana.")