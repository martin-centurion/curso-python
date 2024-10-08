"""
Ticket de compra
¡Vamos a crear tu propio ticket de compra! El desafio es escribir un programa que le pida al usuario el nombre, la cantidad y el valor unitario de tres productos. Después, tu programa tiene que calcular el importe de IVA(21%) de cada uno y mostrar en la terminal un ticket de compra con todos los datos.
"""

# ENTRADAS
# Solicitar nombre(str), la cantidad(int-float) y valor unitario(float) de 3 productos.
# Es aconsejable usar un bucle tipo while pero en este caso se aplica de esta manera primitiva
nombre_producto1 = input("Ingrese nombre de producto 1: ")
cantidad_producto1 = float(input("Ingrese cantidad de producto 1: "))
precio_producto1 = float(input("Ingrese precio producto 1: "))
print(" ")

nombre_producto2 = input("Ingrese nombre de producto 2: ")
cantidad_producto2 = float(input("Ingrese cantidad de producto 2: "))
precio_producto2 = float(input("Ingrese precio producto 2: "))
print(" ")

nombre_producto3 = input("Ingrese nombre de producto 3: ")
cantidad_producto3 = float(input("Ingrese cantidad de producto 3: "))
precio_producto3 = float(input("Ingrese precio producto 3: "))
print(" ")

# PROCESAMIENTO
# Calcular el costo total de cada producto sin IVA
costo1 = cantidad_producto1 * precio_producto1
costo2 = cantidad_producto2 * precio_producto2
costo3 = cantidad_producto3 * precio_producto3

# Calcular el importe del IVA (21%) por cada producto
iva1 = costo1 * 0.21
iva2 = costo2 * 0.21
iva3 = costo3 * 0.21

# Calcular el costo total de cada producto + IVA 
total_con_iva1 = costo1 + iva1
total_con_iva2 = costo2 + iva2
total_con_iva3 = costo3 + iva3


# Calcular el total neto y el total con el IVA
total_neto = costo1 + costo2 + costo3
total_general = total_con_iva1 + total_con_iva2 + total_con_iva3

# SALIDA
# Mostrar el detalle del producto más el costo total
print("-------- TICKET DE COMPRA --------")
print("Producto\tCantidad\tPrecio Unitario\t Total")
print(f"{nombre_producto1:16}{cantidad_producto1}\t\t ${precio_producto1}\t ${total_con_iva1}")
print(f"{nombre_producto2:16}{cantidad_producto2}\t\t ${precio_producto2}\t ${total_con_iva2}")
print(f"{nombre_producto3:16}{cantidad_producto3}\t\t ${precio_producto3}\t ${total_con_iva3}")
print("-------------------------")
print(f"Total Neto: ${total_neto:.2f}") # .xf indica la cantidad de decimales
print(f"Total General: ${total_general}")