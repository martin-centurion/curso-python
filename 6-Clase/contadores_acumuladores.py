#Contadores Acumuladores

"""
Imagina que quieres calcular el promedio de las 
temperaturas diarias durante una semana.
Cada día ingresas una temperatura  lugo se calcula
el promedio al final de la semana.
"""

""" #contador
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
print(f'El promedio de temperatura de promedio de la semana es: {promedio:.2f} C') """

"""
En un videojuego, un personaje comienza con 100 puntos de vida.
Cada vez que recibe un ataque, pierde una cierta cantidad de vida.
Crea un programa que simule los ataques hasta que la vida del personaje
llegue a 0 o menos. Muestra en cada ataque cuánta vida le queda
al personaje.
"""

vida_personaje = 100

while vida_personaje > 0:
    danio = int(input('Ingrese el daño recibido por el ataque: '))
    vida_personaje = vida_personaje - danio
    print(f'Recibiste {danio} puntos de daño, te quedan {vida_personaje} puntos de vida.')

print('El personaje ha sido derrotado!')

