#Contadores Acumuladores

"""
Imagina que quieres calcular el promedio de las 
temperaturas diarias durante una semana.
Cada día ingresas una temperatura  lugo se calcula
el promedio al final de la semana.
"""
#contador
contador_dias = 1
#acumulador
suma_temperaturas = 0

while contador_dias <= 7:
    temperatura = float(input(f'Ingrese la temperatura del día {contador_dias}:  '))
    #acumulando las temperaturas
    suma_temperaturas = suma_temperaturas + temperatura
    #incrementa el contador
    contador_dias = contador_dias + 1

#calcular el promedio de temperaturas
promedio = suma_temperaturas / 7
print(f'El promedio de temperatura de promedio de la semana es: {promedio:.2f} C')