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

print(f"La suma de los numeros es: {suma}");
print(f"La resta de los numeros es: {resta}");
print(f"La multiplicación de los numeros es: {multiplicacion}");
print(f"El modulo de los numeros es: {modulo}");

