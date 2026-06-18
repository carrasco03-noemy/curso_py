## LIBRERIAS ESTANDAR DE PYTHON

# 1. ¿Qué son?

Son 214 módulos oficiales que vienen instalados con Python. No necesitan pip. Su código está en la carpeta Lib/ de tu instalación de Python.

## 2. Top 10 más usados 2026 - con caso real

MóduloP ara qué Función clave Ejemplo real
`os`Sistema operativo`os.listdir()`Listar archivos de carpeta
`sys`Intérprete Python`sys.argv`Leer argumentos de consola
`json`Datos JSON`json.load()`Leer config de API
`datetime`Fechas/horas`datetime.now()`Timestamp de logs
`re`Regex`re.search()`Validar email/ teléfono
`pathlib`Rutas modernas`Path.home()`Manejar archivos multiplataforma
`collections`Estructuras extra`Counter()`Contar frecuencia de palabras
`subprocess`Comandos consola`run()`Ejecutar `git status` desde Python
`argparse`CLI`ArgumentParser()`Hacer script.py --input file.txt
`logging`Logs`logging.info()`Guardar errores en archivo

### 3. Librerías ocultas que pocos usan

1. `zoneinfo` → Timezones sin instalar pytz. Python 3.9+
2. `dataclasses` → Creas clases con @dataclass en 3 líneas
3. `statistics` → Media, mediana, desviación sin numpy
4. `difflib` → Comparar 2 textos y sacar diferencias
5. `ipaddress` → Validar y manipular IPs: ipaddress.IPv4Address('192.168.1.1')

#### 4. Formas de incluirlas en tu archivo

Sintaxis:
import os     # Importa módulo completo
from datetime import date    # Importa solo date
from collections import Counter as C  # Con alias
import os.path as path     # Submódulo con alias
Orden recomendado PEP 8:
import os           # 1. Std library
import sys
from datetime import datetime
import requests   # 2. Librerías externas pip
import pandas as pd

from mi_modulo import funcion  # 3. Tus módulos
Pro tip:`from modulo import` * está prohibido en código profesional. Trae todo y puedes pisar variables sin querer.

# MODULOS EN PYTHON

1. Definición exacta
Módulo = 1 archivo .py que contiene código Python. Es la unidad mínima de reutilización.

Ejemplo: calculos.py
PI = 3.1416
def area(r): return PI * r**2
Al hacer import calculos, Python carga ese archivo completo en memoria.
2. Ciclo de vida de un import

1. Búsqueda: Python revisa sys.path → carpeta actual > std library > site-packages
2. Compilación: Si es primera vez, crea *pycache*/calculos.cpython-312.pyc 
3. Ejecución: Corre el código del .py 1 sola vez
4. Cache: Lo guarda en sys.modules['calculos']. Si vuelves a importar, usa el cache

3. Tipos de módulos

Tipo Dónde está Ejemplo Velocidad
*Built-in* Dentro del .exe de Python`sys`, `time` Más rápido
*Fuente*`.py` en disco`os.py`Rápido
*Extensión C*`.pyd` / `.so` numpy Muy rápido
4. Paquetes
Cuando tienes muchos módulos, los metes en carpeta = paquete:
utils/
├──  init_.py   # Hace que la carpeta sea paquete
├── archivos.py
└── redes.py

Desde Python 3.3 *init*.py puede estar vacío. Se usa para controlar from utils import * con *all*.
5. 5 reglas

1. Nombres: Todo minúscula, sin espacios: mi_modulo.py no MiModulo.py
2. No sombrear: Nunca crees os.py o random.py porque rompes la std library
3. Docstring arriba: Todo módulo debe explicar qué hace en las primeras 3 líneas
4. Guard: Usa if *name* == "*main*": para código de pruebas
5. Import al inicio: Todos los import van arriba, ordenados por PEP 8.