#1# CREAR UN PROGRAMA QUE ME PERMITA AGREGAR A MI LISTA DE COMPRAR LOS SIGUIENTES
#  INGREDIENTES(TRUCHA,CEBOLLA,LIMON,CULANTRO,AJI LIMO,PAPA,CANCHA)
ingredientes:list[str]=[]
for i in range(8):
    ingrediente:str=input("ingresa un ingrediente: ")
    ingredientes.append(ingrediente)
print("lista de compras")  
print(ingredientes)

## CREAR UN PROGRAMA QUE AGREGE AL PRINCIPIO DE LA LISTA DEL GRUPO DE LOS PAISES
#  PARTICIPANTES EN EL MUNDIAL
grupo_a:list[str]=[]
grupo_a.insert(0,"rep. checa")
# ["rep. checa"]
grupo_a.insert(0,"corea del sur")
#["corea del sur","rep. checa"]
grupo_a.insert(0,"sudafrica")
#["sudafrica","corea del sur","rep. checa"]
grupo_a.insert(0,"mexico")
#["mexico","sudafrica","corea del sur","rep. checa"]
print (grupo_a)