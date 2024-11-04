"""
Imagina que estas ayudando a una tienda de videojuegos a
organizar su inventario. El dueño te pide que escribas un
programa que verifique si hay stock suficiente de un
videojuego y, si no hay, que avise que hay que reponerlo.

El programa deberia pedirle al usuario que ingrese
la cantidad actual de stock y, en base a esa cantidad,
mostrar si se necesita hacer un nuevo pedido o no.
"""

stock_minimo = 5

stock_actual = int(input('Ingrese la cantidad de stock: '))

if stock_actual < stock_minimo:
    print('Stock Bajo. Es necesario hacer un nuevo pedido')
else:
    print('Stock suficiente.')
    
"""
Escribe un programa en Python que solicite al usuario el
monto total de la compra y la cantidad de artñiculos que está
comprando. El programa debe determinar el descuento aplicable
según las siguientes reglas:
1) Si la cantidad de artículos comprados es mayor o igual a 5 y
el monto total es mayor a $10000, aplica un descuento del 15%.
2) Si la cantidad de artículos comprados es menor a 5 pero mayor
o igual a 3, aplica un descuento del 10%.
3) Si la cantidad de artículos comprados es menor a 3,
no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra
después de aplicar cualquier descuento o simplemente
el monto original si no hay descuento.
"""

monto_final = float(input('Ingresa el monto total de compra: '))
cantidad_productos = int(input('Ingrese cantidad de productos: '))

descuento = 0

if cantidad_productos >= 5 and monto_final > 10000:
    descuento = 0.15
elif cantidad_productos >= 3 and cantidad_productos < 5:
    descuento = 0.10
else:
    descuento = 0
    
monto_descuento = monto_final * descuento
monto_final_con_descuento = monto_final - monto_descuento

print(f'El monto total de aplicar descuento es: ${monto_final_con_descuento}') 
    