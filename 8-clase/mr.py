productos= [['pizza',10], ['papas',19], ['cebolla',7], ['tomate',2]]

condicion = True
indice = 0

while condicion:
    # pedimos que ingrese una opcion
    eleccion= int(input('si quiere agregar un producto a la lista ingrse 1, si desea ver nuevamente la lista ingrese 2, si desea salir ingrese 3: '))
    if eleccion == 1: #opcion de agregar un producto
        prod_agregar= input('ingrese el nombre del producto que desea agregar: ')
        cant_agregar= int(input('ingrese la cantidad del producto que desea agregar: '))
        for product in productos:
            if product[0] == prod_agregar:
                product[1] += cant_agregar  # Si existe el producto, sumamos la cantidad
                print(f"Producto actualizado: {prod_agregar} ahora tiene {product[1]} unidades.")
                break
        else:
            # se ejecuta solo si no se encontró el producto
            productos.append([prod_agregar, cant_agregar]) #agrega el nuevo producto
            print(f"Producto agregado: {prod_agregar} con {cant_agregar} unidades.")    
        indice = 0
        
    elif eleccion ==2: #opcion de mostrar los productos
            indice= 0
            while indice<len(productos): # recorre la lista y los va mostrando por consola
                producto = productos[indice]
                print("Producto:", producto[0])
                print("Cantidad disponible:", producto[1])
                indice= indice+1
                
                   
            
    elif eleccion ==3: #opcion de salir
         print('Saludos!')
         condicion = False
    else:
        print('No existe esa opcion')