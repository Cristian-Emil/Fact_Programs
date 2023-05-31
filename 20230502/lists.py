a = 'ceva'

lista_mea = ['Ana', True, 12.3, 'Viorel', 10, 'Gabi']
lista_mea.append(20)
lista_mea.append('Ana')

# lista_mea.remove('Ana')

lista_mea[2] = 'Costel'

# print(a[0])
print(lista_mea[0])
print(lista_mea[1])
print(lista_mea[2])
print(lista_mea[3])
print(lista_mea[4])
print(lista_mea[5])
print(lista_mea[6])
print(lista_mea[7])

print(f'lista_mea are {len(lista_mea)} elemente')

val = lista_mea.pop()
print(val)
print(f'lista_mea are {len(lista_mea)} elemente')

i = lista_mea.index('Viorel')
i2 = lista_mea.index('Viorel')
print(f'\'Viorel\' se afla pe pozitia {i}')
lista_mea[i] = 'Stefan'
print(lista_mea)

lista_litere = list('stringul meu')
print(lista_litere)

