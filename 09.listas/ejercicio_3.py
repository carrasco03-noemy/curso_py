alumnos:list[str]=['deduardo','noemy','victor','emerson','yo']
print(alumnos)
# eliminar por valor
alumnos.remove('yo') # ELIMINA EL ULTIMO ELEMENTO
print(alumnos)
# eliminar el ultimo valor por defecto
alumnos.pop()
# EL METODO POP TIENE LA CARACTERISTICADE RECUPERAR EL 
# ELEMENTO ELIMINADO ESO QUIERE DECIR QUE PODEMOS ALMACENAR EN UNA VARIABLE
## pop tambien elimina elementos por indice
a=alumnos.pop(1)
print(f"elimine: {a}")
print(f"mi lista de desaprovados sera: {alumnos}")

## TENGO UNA LISTA DE MARCAS DE VIHICULOS(TOYOTA,NISSAN,DETSUN,
# DAEWOD,SIMO MACK,MAZNA,HONDA),CREAR UN PROGRAMA QUE REALIZE LO SIGUIENTE
"""
1. ELIMINAR EL 5 ELEMENTO
2. EN SU LUGAR AGREGAR LA MARCA MITSUBISHI
3. BUSCAR NISSAN Y MOSTRAR SU VALOR POR TERMINAL
4. MOSTRAR SI EXISTE HONDA EN MI LISTA DE VIHICULOS
"""

"""""""""""""""""""""""""""""""""
  LISTA DE MARCAS DE VEHICULO
"""""""""""""""""""""""""""""""""

marcas: list[str] = ["TOYOTA","NISSAN","DATSUN","DAEWOO","SIMO MACK","MAZDA","HONDA"]

"""
   ELIMINAR EL 5° ELEMENTO
"""
marcas.pop(4)

"""
   AGREGAR MITSUBISHI EN SU LUGAR
"""
marcas.insert(4, "MITSUBISHI")

"""
   BUSCAR NISSAN Y MOSTRAR SU POSICION
"""
buscar: int = marcas.index("NISSAN")
print("NISSAN se encuentra en la posición:", buscar)

"""
 MOSTRAR SI EXISTE HONDA
"""
existe: bool = "HONDA" in marcas
print("¿Existe HONDA?:", existe)

"""
 MOSTRAR
"""
print(marcas)