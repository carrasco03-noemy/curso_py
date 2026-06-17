## CREAR UNA LISTA DE 5 ANIMALES VERTEBRADOS Y 5 ANIMALES INVERTEBRADOS EL ORDEN DEBERA SER ALEATORIO,
# TENDRAS QUE HACER LAS SIGUIENTES CORRECIONES  
"""
1. MODIFICAR LOS 3 PRIMEROS ELEMENTOS POR AVES
2. MODIFICAR EL 6 Y ULTIMO ELEMENTO POR REPTILES
3. MODIFICAR EL ELEMTO 8 POR GUIANFRANCO
4. MOSTRAR TODA LA LISTA NUEVA CON LAS MODIFICACIONES
"""
animales = ["perro", "araña", "gato", "pulpo", "caballo","medusa", 
"pez", "hormiga", "rana", "estrella de mar"]
# 1
animales[0] = "águila"
animales[1] = "loro"
animales[2] = "paloma"
# 2
animales[5] = "serpiente"
animales[-1] = "cocodrilo"
# 4
animales[7] = "gianfranco"

print(f"mi lista modificada es:{animales}")
