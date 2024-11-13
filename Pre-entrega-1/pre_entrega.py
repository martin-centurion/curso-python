productos = [['iphone', 10], ['samsung', 19], ['motorola', 7], ['huawie', 2]]

condicion = True
indice = 0

while condicion:
    eleccion = int(input('Si quieres agregar un producto a la lista ingresa 1, Si desea ver la nuevamente la lista ingrese 2, si desea salir ingrese 3: '))
    if eleccion == 1:
        prod_agregar = input('Ingrese el nombre del producto que desea agregar: ')
        cant_agregar = int(input('Ingrese la cantidad del producto que desea agregar: '))
        for product in productos:
            if product[0] == prod_agregar:
                product[1] += cant_agregar #Si existe el producto, sumamos la cantidad
                print(f'Producto actualizado: {prod_agregar}, ahora tiene {product[1]} unidades.')
                break
        else:
            productos.append([prod_agregar, cant_agregar]) #Agrega el nuevo producto
            print(f'Producto agregado: {prod_agregar} con {cant_agregar} unidades.')
        indice = 0
    
    elif eleccion == 2:
        indice = 0
        while indice < len(productos):
            producto = productos[indice]
            print('Producto: ', producto)
            print('Cantidad disponible: ', producto)
            indice = indice +1
    elif eleccion == 3:
        print('Saliendo del programa')
        condicion = False
    else:
        print('No existe esa opción.')