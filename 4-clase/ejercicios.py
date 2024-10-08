"""
Escribe un programa que calcule cuánto tiempo tardará un viaje en coche. El programa debe solicitar al usuario la distancia total del viaje (en kilometros) y la velocidad promedio del coche (en km/h).
Utilizando estos datos, calcula el tiempo que tardara el viaje (en horas).
"""

#ENTRADAS
#Distancia (float) - velocidad (float)

distancia = float(input("Ingrese la distancia en KM: "))
velocidad_promedio = float(input("Ingrese velocidad promdedio (KM/H): "))

#PROCESAMIENTO
#Calcular el tiempo con la formula de velocidad
tiempo = distancia / velocidad_promedio

#SALIDA
#Mostrar el valor del tiempo en horas
print(f"El tiempo estimado de viaje en horas es: {tiempo:.2f}")

"""
Escribe un programa que calcule el precio final de un producto despues de aplicarle un descuento. El programa debe solicitar el precio original del producto y el porcentaje de descuento. Luego, calcula y muestra el precio con descuento
"""

"""
Crea un programa que convierta una cantidad de datos de gigabytes (GB) a megabytes (MB) y kilobytes (KB).
El programa debe solicitar al usuario la cantidad de gigabytes y luego realizar las conversiones necesarias
"""