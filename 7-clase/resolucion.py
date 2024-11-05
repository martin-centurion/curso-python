"""
Desarrolla un programa que permita al usuario ingresar el nombre de varios productis
y la cantidad de stock que hay de cada uno. El programa debe seguir pidiendo que ingrese 
...
"""

contador_productos = 0
acumulador_stock = 0

while True:
    producto = input('Ingrese el nombre del producto(o "salir" para finalizar): ')
    
    if producto.lower() == "salir":
        break
    
    stock = int(input(f'Ingrese la cantidad de stock de {producto}: '))
    contador_productos += 1 # contador_productos = contador_productos + 1
    acumulador_stock += stock
    
print(f'Cantidad total de productos ingresados: {contador_productos}')
print(f'Total de stock general de productos: {acumulador_stock}')



