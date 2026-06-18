## MODULOS Y LEBRERIAS ESTANDAR

# Libreria estandar typing tipar datos a list y diccionarios para hacer optimo el codigo

# Modulo es una porcion de codigo utilizable,para poder usarlo necesitamos inportar la parte del codigo que deseamos utilizar .

# En este codigo estoy importando desde 1 libreria typing la funcion union

# Union me permite tipar una coleccion de tipos que si no sabes el tipo de dato con posible tipo de datos que puede tener mi valor.

from typing import Union
# sin libreria
# alumno:dict[str:str|int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id-alumno":1,
    "dni":78654328,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}

## ACCEDER
# CLASICA
print(alumno["dni"])
print(alumno["tricula"])

# codigo erroneo print(alumno.get("edad"))
## METODOS 
print(alumno.get("edad","valor encontrado"))
## CREAR/MODIFICAR UN VALOR
print(alumno)
alumno["nombre"]="otro" # si existe la clave actualiza enl valor
print(alumno)
alumno["ruc"]=90876543267 # si no existe la clave lo crea
print(alumno)

## CREAR/MODIFICAR VARIOS
alumno.UPDATE({"nombre":"celia","edad":15})
print(alumno)
alumno.UPDATE({"carrera":"agro","semestre":"III"})
print(alumno)

## ELIMINAR
eliminado=alumno.POP("carrera")
print(f"el elemento eliminado es {eliminado}")
print(f"mi nuevo diccionario {alumno}")





