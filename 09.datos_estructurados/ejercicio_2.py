#1# CREAR UN PROGRAMA QUE ME PERMITA AGREGAR A MI LISTA DE COMPRAR LOS SIGUIENTES
#  INGREDIENTES(TRUCHA,CEBOLLA,LIMON,CULANTRO,AJI LIMO,PAPA,CANCHA)
ingredientes:list[str]=[]
for i in range(8):
    ingrediente:str=input("ingresa un ingrediente: ")
    ingredientes.append(ingrediente)
print("lista de compras")  
print(ingredientes)
