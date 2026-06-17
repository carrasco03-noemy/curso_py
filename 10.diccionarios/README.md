## 📓 DICCIONARIOS
🏷️ *Los dicionarios son la forma mas comun de almacenar datos estructurados de objetos que nos rodea en el mundo ,al igual que las listas que guardan informacion en `ELEMENTOS`,de igual manera los diccionarios almacenan sus datos en `ELEMENTOS`separados por comas.
La diferencia es que las listas almacenan los elementos por `INDICE`y `VALOR`.
Y los diccionarios almacenan los elementos por `CLAVE:VALOR`.*

**📎 EJEMPLO**

```python
vocales:list[str]=['a','e','i','o','u']→valor
# indices           0   1   2   3   4
# un elemento en una lista esta conformado por dos cocitas el indice y su valor.
# para acceder a un valor en una lista
vocales[2] # → i
# un elemento en un diccionario esta conformado por clave:valor
alumno:dict={'nombre':'eduardo','edad':40}
# para acceder a un diccionario
alumno["nombre"]# → eduardo
```

## 📌ACCEDER A ELEMENTOS

- **🔍POR CLAVE(forma directa)**

```python
persona:dict={
    "nombre":"celia",
    "edad":16
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona["edad"]) # → 16
print(persona["email"]) # → celi@email.com
```

- **🔍POR SU METODO(formamas segura)**

```python
persona:dict={
    "nombre":"celia",
    "edad":16
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona.get("nombre")) # → celia

# la diferencia de este metodo es que no permite manejar errores 
print(persona.get("telefono")) # → NONE

print(persona.get("telefono","no disponible")) # → si la clave telefono no existe no mostrara NONE si no el segundo parametro que le pasemos al metodo get.
```

## 🪄 MODIFICAR ELEMENTOS

- **CAMBIAR UN VALOR EXISTENTE**

``` python
persona:dict={
    "nombre":"celia",
    "edad":16
}
persona["edad"]= 19
# Agregar una nueva clave:valor
persona["carrera"]="agro"
# Si la clave no existe se crea automaticamente.si existe se actualiza.
```

## 🔍🔁AGREGAR/ACTUALIZAR MULTIPLES ELEMENTOS

Para eso tenemos que hacer uso del metodo `.UPDATE` se puede agregar si los pares de `clave:valor` no existe y actualizar si el `clave:valor` existe.

```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "RUC":20465783674
}
# Actualizar usando el metodo .UPDATE tengo dos maneras de usar este metodo

# 1. 📖 DICCIONARIOS
tienda.UPDATE({"RUC":23456789023,"telefono":987654321})
# 2. 📎PARES CLAVE:VALOR
tienda.UPDATE(h_atencion="9-12",gerente="luis")
```

## ❌🗑️ ELIMINAR ELEMENTOS

```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "RUC":20465783674
}
el_eliminado=tienda.POP("RUC")

#Para limpiar todo el diccionario
tienda.CLEAR()
