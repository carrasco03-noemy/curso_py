# los metodos son funciones 
texto_minuscula:str="hola"
print(texto_minuscula.upper())
# metodo para convertir un texto en minusculas
texto_mayuscula:str="HOLAAA"
print(texto_mayuscula.lower())
# metodo para convertir solo la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
#metodo para convertir la primera letra de cada palabra en mayuscula como un titulo
print(texto.title())
#metodo para quitar espacios
texto_espacio:str=" osos"
print(texto_espacio)
# este metodo quita los espacios que estan a la derecha e izquierda.si deseamos quitar solo los espacios de la izquierda usamos el metodo lstrip() y si deseamos quitar los espacios solo de la derecha usamos rstrip()
print(texto_espacio.strip())

# metodo para buscar un caracter o un conjuntode caracteres
# fin retorna el indice donde comiensa el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo ami mama de noemy"
print(parrafo.find("noemy"))
print(parrafo[34:])
# metodo para remplazar una parte del texto
texto_incorrecto:str="el leon es malo"
print(texto_incorrecto.replace("malo","bueno"))
 #(metodo) operador binario de existencia
#este operador verifica si cierto texto existe o no dentro de otro retorna True si existe y False si no exsiste
vocales:str="aeiouAEIOU"
print("a"in vocales)
#lo que esta dentro son expreciones en programacion son datos
 # tarea que son y cuale son los operadores unarios,binarios,ternarios en python

 ## OPERADOR UNARIO 
 #trabaja con un solo dato, se utiliza para modificar directamente ese valor ,por ejemplo cambiar su signo o negar una condicion
x=5
print(-x)
#resultado:-5

## OPERADOR BINARIO
#trabaja con dos datos,son los mas usados y permite realizar operaciones matematicas,comparaciones o logicas
a=4
b=2
print(a+b)
#resultado:6

## OPERADOR TERNARIO
#sirve para decidir rapido (como un if corto),trabaja con tres partes (condicion + dos resultados)se usa para tomar decisiones rapidas en una sola linia 
edad=17
print("mayor"if edad>=18 else "menor")
# resultado: menor

##REALIZAR UN PROGRAMA QUE NOS PIDA LA CONTRASEÑA SI LA CONTRASEÑA ES CORRECTA EL USUARIO PODRA INGRESAR CASO CONTRARIO LE DARA UN MENSAJE DE CONTRASEÑA INCORRECTA

password_user:str=input("ingresa tu contraseña:")
print("bienvenido al sistema"if password_user=="hola1234"else"contraseña incorrecta")
