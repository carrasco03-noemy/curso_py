#1# DESEAMOS AGREGAR EN UNA LISTA VACIA LOS NOMBRES DE LOS PAISES QUE PARTICIPARAN
# EN EL MUNDIAL DESARROLLAR EL PROGRAMA QUE HAGA POSIBLE ESTA TAREA
#1# FORMA
paises:list[str]=[]
paises.append("peru")
paises.append("bolivia")
paises.append("chile")
print(paises)
#2# FORMA
pais:str=input("ingresa el nombre del pais: ")
paises.append(pais)
print(paises)
#3# FORMA UN BOOQLE PARA REPITER 5 VESES 
# VARIAS HAY DOS TIPOS 
# uno mas facil para realizar
range:int=int(input("ingrese la cantidad de pais que desea agregar: "))

for i in range(5):
    nuevos_paises:str=input("ingresa un pais: ")
    paises.append(nuevos_paises)
print(paises)    
