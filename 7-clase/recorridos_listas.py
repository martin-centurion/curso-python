"""
Crear una lista de libros con su titulo, autor y cantidad
de copias disponibles. Mostrar los libros
"""

biblioteca = []
num_libros = int(input('Cuantos libros vas a ingresar?'))

contador = 0
while contador < num_libros:
    titulo = input('Ingrese el titulo del libro: ')
    autor = input(f'Ingrese autor de "{titulo}": ')
    copias = int(input('Ingrese cantidad de copias: '))
    
    libro = [titulo, autor, copias]
    #libro = (titulo, autor, copias)
    biblioteca.append(libro)
    contador += 1

indice = 0 #i
while indice < len(biblioteca):
    libro_mostrar = biblioteca[indice]
    print(f'Titulo: {libro_mostrar[0]}, Autor: {libro_mostrar[1]}, Copias: {libro_mostrar[2]}')
    indice += 1