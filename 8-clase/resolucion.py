"""
Tu programa debe permitir al usuario consultar el inventario de
una tienda para verificar si un producto está en stock.
Si el producto está en la lista, el programa debe informarlo, si no,
debe mostrar un mensaje indicando que no está disponible
"""

inventario = ['manzanas', 'leche', 'tomates', 'arroz']

producto_a_buscar = input('Ingrese el nombre del producto: ')

indice = 0
encontrado = False

while indice < len(inventario):
    if inventario[indice].lower() == producto_a_buscar:
        encontrado = True
        break
    indice += 1
    
if encontrado:
    print(f'El producto {producto_a_buscar} esta en stock.')
else:
    print(f'El producto {producto_a_buscar} no esta disponible.')
    