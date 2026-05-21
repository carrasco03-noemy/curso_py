#OPERACIONES ARITMETICAS CON NUMEROS EN PYTHON
# 1.SUMA -OPERADOR BINARIO
# 🔴variables globales
## son datos que se puede utilizar en cualquier parte del software que este construyendo
# 🔴variables locales
## son datos que solo son accesibles en pequeñas porciones de codigo o "scope"
firts_numb:int|float=20
second_numb:int|float=5
# SUMA
print(f"la suma de {firts_numb}+{second_numb}={firts_numb+second_numb}")
#RESTA
print(f"la resta de {firts_numb}-{second_numb}={firts_numb-second_numb}")
#DIVICION
print(f"la divi de{firts_numb}/{second_numb}={firts_numb/second_numb}")
#MULTIPLICACION
print(f"la multi de{firts_numb}*{second_numb}={firts_numb*second_numb}")
#DIVI EXAC
print(f"la divi exac de {firts_numb}//{second_numb}={firts_numb//second_numb}")
#INCREMENTO(++)-operador unario
firts_numb+=1
print(f"el incremento de {firts_numb}")
#DECREMENTO()
firts_numb-=1
print(f"el decremento de {firts_numb}")
#POTENCIACION (**)
print(f"la potenciacion de {firts_numb}**{second_numb}={firts_numb**second_numb}")
