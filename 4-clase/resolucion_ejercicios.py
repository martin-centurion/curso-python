"""
Crea un programa que solicite al usuario dos numeros enteros.
Realiza las siguientes o peraciones: suma, resta, multiplicación, y módulo.
Muestra el resultado de cada operación en un formato claro y amigable.
"""

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
modulo = numero1 % numero2

print(f"La suma de los numeros es: {suma}")
print(f"La resta de los numeros es: {resta}")
print(f"La multiplicación de los numeros es: {multiplicacion}")
print(f"El modulo de los numeros es: {modulo}")

"""
Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.

Utilizando operadores aritméticos, calcula la cantida de propinas y el total a pagar (incluyendo la propina).
Finalmente, muestra los resultados en la pantalla.
"""

monto_total = float(input("Ingrese el monto total: "))
porcentaje_propina = float(input("Porcentaje de propina: "))

propina = monto_total * (porcentaje_propina / 100)

total_pagar = monto_total + propina

print(f"La cantidad de propina es: ${propina}")
print(f"El total a pagar incluida la propina es: ${total_pagar}")

"""
Rubros:

Ecommerce donde se pueda aplicar el conocimiento de Python:

Seleccionar rubro: Tienda de Ropa - JCR INDUMENTARIA

Aplicar CRUD - Create / Read / Updated / Delete
Donde se puede eliminar el producto, modificar, cargar y eliminar
el diseño debe ser minimalista.

Colores solidos: 
Violeta #220B42 - #6D30C4
Naranja #FF8400 - #FFA23E
Blanco #FFFFFF

Tratar de que estos colores sean pasteles - Buscar una paleta de
colores acorde al ecommerce desarrollado.

"""

