# 🧱 DATOS ESTRUCTURADOS 
- tenemos 2 tipos de datos primarios (string, numerico, booleno)
- tenemos 2 tipos de datos estructurados (listas, diccionarios)
## 📋 LISTAS
son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener:
- listas de tipo numerica
- listas de tipo texto
- listas de tipo mixto

python nos permite acceder a estas listas a travez de indices, los indices son ascendentes empesando del numero 0.
### CREACION DE LISTAS 
para crear listas solo hasta encerrar los elementos que deseamos alamcenar con `[]` inmediatamente despues del operador de asignacion `=`
```python
# Creando una LISTA VACIA
listas:list=[] # lista vacia # list anotacion indica que tipo de dato va almacenar 
# LISTA NUMERICA
# OJO: Los elementos de una lista  se separa por comas  
lista_numerica:list[int]=[3,8,4]
listas_num_mixto:list[int|float]=[3.6,7,.7]
# LISTA TEXTO
amigos:list[str]=['eduardo','kevin']
# LISTA MIXTA
lista_mixta: list=['pedro',20,false,1.67]
```
## ACCEDER Y MODIFICAR ELEMENTOS DE UNA LISTA
para poder accerder a un elemento de la lista trabajamos con los indices que python le asigna a cada elemento que tenemos:
- los indices positivos (comienzan de 0 y van de izquierda a derecha)
-  los indices negativos (comienzan de -1 y van de derecha a izquierda)
con estos indices podemos acceder al valor del elemento y tambien podremos modificarlos.
- Aceder y modificar por indice (posicion)
```python
## aceder a elemetos
frutas:list[str]=[🍎,🍊,🍒]
# posicion o indice
# ACCEDER AL TERCER ELEMENTO
print(frutas[2])
# ACCEDER AL 2 ELEMENTO POR SU INDICE NEGATIVO
print(frutas[-3])
# Modificar
frutas[3]=
# ACCEDER POR RANGO
print(frutas[0:2])
# DESDE LA POSICION 1 HASTA LA 3
print(frutas[1:3])
# DESDE EL INICIO HASTA LA POSICION 2
print(frutas[:2])
# DESDE LA POSICION 1 HASTA EL FINAL
print(frutas[1:])
```
- Acceder y modificar por rango (slicing)
```python
Vocales:str['a','e','i','o','u']
#ACCEDER A ELEMENTOS POR SLICING
# esta tecnica nos permite acceder a mas de un elemento en una sola linia de codigo
Vocales[0:3]

##REMPLAZAR  ELEMENTO POR SLICING
vocales[0:3]=['A','E','I']

```

## DICCIONARIO