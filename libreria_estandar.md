## LIBRERIAS ESTANDAR DE PYTHON

# ¿QUE SON?

Las librerías (o módulos) en Python son conjuntos de código ya escrito que contienen funciones, clases y herramientas listas para usar. Sirven para no tener que programar todo desde cero.

## Las librerías estándar más usadas

1. `os` — Sistema operativo

Permite trabajar con archivos, carpetas y rutas.
```python
import os

print(os.getcwd())  # Directorio actual
```

2. `sys` — Información del intérprete
import sys

```python
print(sys.version)
```

3. `math` — Matemáticas

```python

print(math.pi)
print(math.sqrt(16))
```

También puedes importar funciones específicas:

```python

print(sqrt(16))
4. random — Valores aleatorios
import random

numero = random.randint(1, 100)
print(numero)
```

5. `datetime` — Fechas y horas

```python
from datetime import datetime

ahora = datetime.now()
print(ahora)
```

6. `json` — Manejo de JSON

```python
import json

persona = {
    "nombre": "Juan",
    "edad": 30
}

texto = json.dumps(persona)
print(texto)
```

7. `pathlib` — Manejo moderno de archivos

```python
from pathlib import Path

ruta = Path("archivo.txt")
print(ruta.exists())
``` 

8. `collections` — Estructuras avanzadas

```python
from collections import Counter

datos = ["a", "b", "a", "c", "a"]
contador = Counter(datos)

print(contador)
```

9. `csv` — Archivos CSV

```python
import csv

with open("datos.csv", newline="") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)
```

10. `sqlite3` — Base de datos integrada

```python
import sqlite3

conexion = sqlite3.connect("mi_bd.db")
print("Conectado")
conexion.close()
```

Formas de importar librerías
Importar todo el módulo

```python
import math

print(math.sqrt(25))
```

Importar una función específica

```python
from math import sqrt

print(sqrt(25))
```

Importar varias funciones

```python
from math import sqrt, pi

print(pi)
print(sqrt(49))
```

Usar un alias

```python
import pandas as pd
import numpy as np
```

Con librerías estándar:

```python
import datetime as dt

print(dt.datetime.now())
```

Estructura típica de un archivo Python
# Importaciones

```python
import os
import math
import random
from datetime import datetime

# Variables

nombre = "Carlos"

# Funciones

```python
def saludar():
    print(f"Hola {nombre}")


# Programa principal

saludar()

print(math.pi)
print(random.randint(1, 10))
print(datetime.now())
```

## Las 10 librerías que más usarás al empezar

1- os
2- pathlib
3- math
4- random
5- datetime
6- json
7- csv
8- collections
9- re (expresiones regulares)
10- sqlite3

# MODULOS EN PYTHON

Los módulos de Python son archivos con extensión .py que contienen código reutilizable (funciones, clases, variables, etc.). Su propósito es organizar el código y permitir que puedas reutilizarlo en diferentes programas.

Ejemplo de módulo propio
Archivo: operaciones.py

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
Archivo: main.py
import operaciones

resultado = operaciones.sumar(10, 5)
print(resultado)

Salida:

15
Formas de importar módulos
1. Importar el módulo completo
import math

print(math.sqrt(16))
```

2. Importar una función específica

```python
from math import sqrt

print(sqrt(16))
```

3. Importar varias funciones

```python
from math import sqrt, pi

print(pi)
print(sqrt(25))
```

4. Usar un alias

```python
import math as m

print(m.pi)
```

## Módulos estándar más utilizados

Python incluye muchos módulos listos para usar:

MóDULO    |       FUNCION
math      |  Operaciones matemáticas
random    | Números aleatorios
datetime  |  Fechas y horas
os        | Sistema operativo
sys       |Información del     intérprete
json      |  Manejo de JSON
csv       |Lectura y escritura de CSV
re        | Expresiones regulares
sqlite3   |  Bases de datos SQLite
pathlib   |Manejo de rutas y archivos

Ejemplo:

```python
import random

print(random.randint(1, 100))
```

## ¿Dónde se guardan los módulos?

Python busca módulos en:

1. La misma carpeta del programa.
2. Las carpetas de la biblioteca estándar.
3. Las carpetas donde se instalan paquetes con pip.

Puedes ver las rutas de búsqueda:

```python
import sys

print(sys.path)
```
