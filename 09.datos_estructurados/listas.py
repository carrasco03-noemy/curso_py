lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de la variable no debe tener el tipo de dato que se va almacenar
amores:list[str]=['mama','papa','hermano']
print(f"la cantidad de elementos que tiene la variable amores es: {len(amores)}")

frutas:list[str]=["🍎","🍑","🍒","🍇"]
# posicion o indice
# ACCEDER AL TERCER ELEMENTO
print(frutas[2])
# ACCEDER AL 2 ELEMENTO POR SU INDICE NEGATIVO
print(frutas[-3])

# Modificar el ultimo elemento con una naranja
frutas[-1]="🍊"
print(frutas)
### slicing
Ciudades:list[str]=['lima','ica','chincha','pauza','urcus']
## SI DESEAMOS QUE LOS DATOS EXTRAIDOS SEAN PERSISTENTES OSEA SE MANTEMGAN ALMACENADOS DURANTE
# LA EJECUCUIN DE MI PROGRAMA LOS ALMACENO EN UNA VARIABLE
datos_extraidos:list[str]=Ciudades[-2:]
# SI SOLO DESEO MOSTRAR Y NO ALMACENAR EL SLICING LO REALIZO EN EL PRINT
print(Ciudades [0:3])
print(datos_extraidos)
## REMPLAZO DE ELEMENTOS POR SLICING
num_pares:list[int]=[1,3,5,6,8,10]
print(num_pares)
## REMPLAZAR
num_pares[0:3]=[2,4]
print(f"mi lista modificada es:{num_pares}")