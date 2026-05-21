# para declarar una variable en python usaremos la convencion snakes_case
## reglas
### 1. el nombre de la variable debe indicar que dato se esta almacenando
### 2. las variables no deben contener numeros ni caracteres especiales (@,/,!,?).
nombre_curso="lenguaje de programacion"
creditos_curso=3
horas_semanales_curso=6
# ADVERTENCIA - las variables son mutables
print(creditos_curso) #salida:3
creditos_curso=10
print(creditos_curso) #salida:10

# NOTA INPORYANTE PARA TODO EL CURSO - cada vez que declaremos variables usaremos anotaciones para imdicar que tipo de dato se va almacenar

nombre_alumno:str = "maria"
edad_alumno:int = 28
estatura_alumno:float = 1.59
asistencia_alumno:bool = True
amigos_alumno:list = []
direccion_alumno:dict = {"n_calle":"psj belen", "numero_casa":230,  "barrio":"ccayao"
}
# asignacion de un variable a otra variable
edad_alumno:int=21
edad_docente:int=edad_alumno
## INPORTANTE NO OLVIDARSE
## un decorador en python nos indica que tipo de datos va almacenar nuestra varible
## los decoradores que python trae por defecto son:

########### datos primitivos ##########
# decoradores para datos primitivos
## :int - enteros
## :float - decimales, flotante
## :str - string texto
## :bool - datos boleano true o false

########### datos estructurados ###########
# decoradores para datos estructurados
## :list - listas
## :dict - diccionarios
## como hacemos uso de las vareables
## para ser uso del dato almacenado en una variable basta con hacer el llamado del nombre de  una bariable
primer_numero:int = 30
segundo_numero:int = 20
suma:int = primer_numero+segundo_numero