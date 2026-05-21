# tecnicas para unir string en solo 
## concatenacion 
## para esto usamos el operador de concatenacion +
# cuando este operador se encuentra entrew dos textos se combierte en el operador concatenacion y cuando esta entre dos numeros es el operador de adicion (suna).
nombre:str = "noemy"
apellido:str = "noseprofesor"
nombre_completo:str = nombre+" "+apellido
print(nombre_completo) #salida: noemy no se profesor

## opcion mas optima de concatenacion
print(nombre,apellido)

## f-string (tarea)
# formato de string esto sirve para formatear string con variables de python  y para eso se requiere de un f antes de escribir un string ,si se desa incluir codigo python en el string ,se debe encerrar entre llaves {}.
nombre:str = "gianfranca"
edad:int = 14
# mensaje de salida me diga hola mi nombre es {} y tengo {}
print(f"hola mi nombre es{nombre}y tengo {edad}")

## plantillas de string 
nombre_cliente:str=input("ingrese tu nombre: ")
ruc_cliente:int=int(input("ingrese ruc: "))
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrese codigo: ")
nombre_producto:str=input("ingrese nombre producto: ")
precio_unidad:float=float(input("el precio del producto: "))
catidad_producto:float=float(input("cantidad a comprar: "))
precio_total:float= precio_unidad*"cantidad_producto"

plantilla:str=f"""
cliente.{nombre_cliente}......RUC:{ruc_cliente} direccion:{direccion_cliente}
codigo producto | nombre producto   | p_unidad     | cantidad
-----------------------------------------------------------------------
## {codigo_producto} {nombre_producto} {precio_unidad} odu
------------------------------------------------------------------------
el precio total de su compra es de:{precio_total}
"""
print(plantilla)