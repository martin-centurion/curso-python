# CONDICIONAL DE PYTHON
# EJ: SI LA VARIABLE "X" ES IGUAL A 5
# APLICAR LA ESTRUCTURA IF ELSE

"""
    La estructura condicional
    <(IF)
    SI LA CONDICION ES VERDADERA ENTONCES
    ENTONCES DEBO HACER ALGO
    ...
    >SINO (ELSE)
    EJECUTAR ACCIONES SINO SE CUMPLE
    LA CONDICIÓN
    >FINSI
"""

edad = 16
if edad >= 18:
    print('La persona es mayor de edad')
else:
    print('La persona es menor de edad')
    
# CALCULAR LA CANTIDAD DE CONDICIONES?
# EN UN IF SE PUEDE EVALUAR

# EVALUAR MULTIPLES CONDICIONES - IF ELSE IF

cantidad_productos = 7

# >= 10 -> 10%
# 5 <= ; < 10 -> 5%
# < 5 -> NINGUN DESCUENTO / NO TIENE DESCUENTO

if cantidad_productos >= 10:
    print('Tienes un 10% de descuento')
elif cantidad_productos >= 5:
    print('Tienes un 5% de descuento')
else:
    print('No tiene descuento')
    
pago_aplicacion = True # Tiene que ser un booleano(TRUE o FALSE)

if pago_aplicacion: # pago_aplicacion == True
    print('Tiene descuento adicional del 5%')
    if cantidad_productos >= 10:
        print('Tienes un 10% de descuento')
    elif cantidad_productos >= 5:
        print('Tienes un 5% de descuento')
    else:
        print('No tienes descuentos por productos')
else:
    print('No accediste al descuento por pago aplicación')
    
    



