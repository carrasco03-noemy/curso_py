## UNA FERRETERIA TIENE SEPARADAS EN DOS LISTAS LOS SIGUIENTES 
# PRODUCTOS
""" 
1. LISTA DE PRODUCTOS DE LIMPIEZA (10 PRODUCTOS)
2. LISTA DE MATERIALES DE CONSTRUCCION (10 PRODUCTOS) 
-------------------------------------------------
EL DUEÑO DESEA REALIZAR LAS SIGUIENTES ACCIONES:

1. EN SU LISTA DE PRODUCTOS DE LIMPIEZA EXISTE UN MATERIAL DE
 CONSTRUCCION DEBES DE ELIMINARLO Y PASAR EL PRODUCTO A LA LISTA
 QUE CORRESPONDE
2. INDICAR SI EN LA LISTA DE MATERIAL DE CONSTRUCCION EXISTE CEMENTO
3. EN LA LISTA DE PRODUCTOS DE LIMPIEZA BUSCAR EL PRODUCTO LEJIA Y 
CAMBIAR SU VALOR POR LEJIA SAPOLIO
4. MOSTRAR UN MENSAJE DONDE SE DETALLE CUAL ES LA LISTA DE MATERIAL DE 
CONSTRUCCION Y LA LISTA DE PRODUCTO DE LIMPIEZA FORMATEADO
"""
"""
CREAR MIS LISTA DE PRODUCTOS DE LIMPIEZA Y MATERIALES DE CONSTRUCCION
"""
productos_limpieza:list[str]=['escoba','lejia','trapeador',
'poett','esponja','trapo','desinfectante','ladrillo','cloro','jabon']
materiales_construccion:list[str]=['cemento','ladrillo','brocha',
'pintura','arena','fierro','yeso','clavo','martillo','tubo']

"""
BUSCAR LADRILLO EN LIMPIEZA Y PASARLO A CONSTRUCCION 
"""
elemento_retirado=productos_limpieza.pop(productos_limpieza.index("ladrillo"))
materiales_construccion.append(elemento_retirado)

"""
VERIFICAR SI EXISTE CEMENTO EN CONSTRUCCION 
"""
existe: bool = 'cemento' in materiales_construccion
print(f'Existe cemento: {existe}')

"""
# 3. Buscar lejia y cambiar por lejia sapolio
"""
buscar: int = productos_limpieza.index('lejia')
productos_limpieza[buscar] = 'lejia sapolio'

"""
MOSTRAR MENSAJE
"""
print("PRODUCTOS DE LIMPIEZA")
print(productos_limpieza)

print("MATERIALES DE CONSTRUCCION")
print(materiales_construccion)

mensaje:str=f"""
MI LISTA DE PRODUCTOS DE LIMPIEZA
{productos_limpieza} 
MI LISTA DE MATERIALES DE CONSTRUCCION
{materiales_construccion} 
"""
print(mensaje)