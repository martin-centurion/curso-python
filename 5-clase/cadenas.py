cadena1 = "Hola Cadena"
cadena2 = 'Python es genial'
cadena3 = '''Es una cadena que permite el
            salto de linea'''

# Operacion con cadenas
# Repeteción
parte1 = "Na " * 6 # Si se suma da error
print(parte1)

# Concatenación +
cancion = parte1 + "Batman"
print(cancion)

# Longitud de la cadena
longitud = len(cancion)
print(longitud)

# Slicing - rebanadas
texto = "Python es divertido"
print(texto[18]) # acceder a un caracter por su posición

# Extraer una subcadena - [inicio - fin]
print(texto[0:2])

# Omitir el inicio
print(texto[:8])

# Omitir al final
print(texto[7:])

#agregar un paso/salto - Saltea las posiciones de una cadena de texto
print(texto[0:10:2])

# Uso de indices negativos
print(texto[-9:0]) # Comienza 9 posiciones antes del final hasta el final

# Invertir una cadena
print(texto[::-1])

# Funciones cadenas 
