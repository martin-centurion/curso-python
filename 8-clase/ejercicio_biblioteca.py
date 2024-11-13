"""
Enunciado:
Se debe crear un prgrama que pueda gestionar por medio de un Menu un listado.
Las operaciones que se pueden realizar son:
1. Agrega un libro con su codigo, titulo y cantidad de copias
2. Mostrar el listado de los libros
3. Simular el prestamo de libros, reduciendo la cantidad de copias disponibles
4. Salir
"""

biblioteca = [
    ['001', 'El quijote', 10],
    ['002', 'El principito', 2],
    ['003', 'El señor de los anillos', 5]
]

while True:
    print('\nMenú de Biblioteca')
    print('1. Agrega un libro')
    print('2. Mostrar listado de libros')
    print('3. Prestar un libro')
    print('4. Salir')
    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        #agregar funcionalidad para agregar libros
        codigo = input('Ingrese el codigo del libro: ')
        titulo = input('Ingrese el titulo del libro: ')
        cantidad = int(input('Ingrese la cantidad de copias: '))
        libro = [codigo, titulo, cantidad]
        biblioteca.append(libro)
        print(f'Libro {titulo} agregado correctamente.')
    elif opcion == 2:
        print('\nListado de libros:')
        for libro in biblioteca:
            print(f'Código: {libro[0]} - Titulo: {libro[1]} - Copias: {libro[2]}')
    elif opcion == 3:
        #El usuario ingresa el codigo del libro que quiere (codigo_buscar)
        #Buscar un libro dentro de la biblioteca que tenga ese codigo
        #Si lo encuentra -> Verificar cantidad copiar -> se lo presto (copias -1)
        #Si las copias no estan disponibles -> mostrar "No hay copias disponibles"
        #Si no lo encuentra -> Deberia mostrar que el codigo no existe en la biblioteca
        #if codigo_buscar in biblioteca:   
        pass
    elif opcion == 4:
        print('Saliendo del programa')
        break
    else:
        print('Opcion invalida, intente nuevamente')