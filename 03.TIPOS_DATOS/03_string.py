# 📎este tipo de dato sirbe para almacenar informacion de tipo texto, puede ser texto simple como o texto intenso.
# 🗂️para almacenar un texto de tipo texto la informacion devera estar enserrada entre comillas ("",'',"""""").
## - comillas doble ("")
## - comillas simple ('')
## - docstring ("""""",'''''')

nombre_instituto:str="IESTP_JMA"
nombre_curso:str='lenguaje de pro.'
descripcion_curso:str="""
el curso de "lenguaje de programacion",
tiene una duracion de un semestre
educativo con 6 horas semanales y aprendera a programar en el lenguaje
"python"
"""

##📎 los string tienen fuunciones basicas para poder interactuar con los datos que estamos almacenando
## la estructura de una funcion es la siguiente 
## nombre_funcion(argumento)
## *argumento - es un valor que se le pasa a una funcion , funcion que en base a su programacion retornara a otro valor distinto al pasado por el argumento
print ("hola mundo") # salida: hola mundo
print("hola","mundo") # salida: hola mundo

# funcion para mostrar la cantidad de cracteres que tiene un string-texto
texto:str = "soy de mi mama"
cantidad_caracteres:int = len(texto)
print("cantidad de caracteres:",cantidad_caracteres)

# forma de acceder a un caracter en epecial
## para esto hacemos uso de la notacion de corchetes []
## para esto tenemos que entender que python asigna a cada a cada caracteres con un indise de base cero

# ejemplo: celia
# indices  01234
nombre_celia:str ="celia"
print(nombre_celia)
print(nombre_celia[2])

# troceado de texto
## para esto se utiliza la notacion de corchete con la diferencia que se debe indicar de que indice inicial y un indice del final del texto a extraer.
## texto[i_inicial:i_final]

vocales:str = "aeiou"
print(vocales[1:3])
print(vocales[3:])
print(vocales[:3])