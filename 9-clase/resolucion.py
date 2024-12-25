"""
En una tienda, es necesario actualizar el inventario cuando se venden.
A continuación, te proporcionamos un arreglo con una lista de productos, cada
producto tiene un codigo, una descripción y una cantidad de stock.
"""

productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 50],
    ["P003", "Bananas", 50],
    ["P004", "Naranjas", 50]
]

codigo_a_vender = input('Ingrese el codigo del producto a verder: ')

encontrado = False
indice = 0

while indice < len(productos):
    #hacer la operacion del codigo del producto
    if codigo_a_vender == productos[indice][0]:
        encontrado = True
        break
    else:
        indice +=1

if not encontrado:
    print('Codigo de producto no encontrado en la lista')
else:
    cantidad_vendida = int(input('Ingrese la cantidad vendida: '))
    if cantidad_vendida > 0:
        productos[indice][2] -= cantidad_vendida
        print(f"Venta realizada. Stock actualizado: {productos[indice][2]}")
    else:
        print('La cantidad venddida debe ser mayor a cero.')