lista_ejemplo = [13, 'Hola Lista', 3.14, True]
print(lista_ejemplo)

lista_animales = ['perro', 'vaca', 'leon', 'gato']
print(lista_animales[1])

#OPERACIONES CON LISTAS
#modificar un elemento

lista_animales[0] = "firulai"
lista_animales[2] = "leoncito"
print(lista_animales)

#agregar un elemento al final de la lista
lista_animales.append('mono')
print(lista_animales)

#insertar un elemento en una posicion determinada
lista_animales.insert(2, 'cebra')
print(lista_animales)

#eliminar un elemento dado su valor
lista_animales.remove('vaca')
print(lista_animales)

#elimar un elemento por su indice
del lista_animales[0] #[0:2] de una posicion a otra
print(lista_animales)

#determinar la cantidad de elementos len()
cantidad_animales = len(lista_animales)
print(f'Cantidad de animales: {cantidad_animales}')