"""
Sintaxis
for elemento in secuencia:
    #hacer algo
"""

lista_compras = ['leche', 'cafe', 'harina', 'azucar']

for producto in lista_compras:
    print(f"Necesito comprae: {producto}")
    
#for con tuplas

dias_semana = ('Lunes', 'Martes', 'Miercoles','Jueves', 'Viernes')

for dia in dias_semana:
    print(f"hoy es {dia}")
    
productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 50],
    ["P003", "Bananas", 50],
    ["P004", "Naranjas", 50]
]

for mi_producto in productos:
    print(mi_producto)

#RANGOS
# range(inicio, fin, paso)
# contar hasta 10
range(0, 10, 1) #range(10)

for numero in range(10):
    print(f"Numero: {numero}")

#numeros pares de 2 a 10

for numero_pares in range(2, 11, 2):
    print(f"Numeros pares: {numero_pares}")
    
#numeros impares de 1 a 10

for numero_impares in range(1, 10, 2):
    print(f"Numeros impares: {numero_impares}")
