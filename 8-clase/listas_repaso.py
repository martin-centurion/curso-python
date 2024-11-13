listas_frutas = ['manzanas', 'limon', 'sandia']

print(listas_frutas[1])

listas_frutas.append('cereza')
print(listas_frutas)

#Operador IN
print('limon' in listas_frutas)

print('uva' in listas_frutas)

#index - nos devuelve la posición
print(listas_frutas.index('limon'))

#ESTRUCTURA REPETITIVA FOR
for fruta in listas_frutas:
    print(f'Fruta: {fruta}')