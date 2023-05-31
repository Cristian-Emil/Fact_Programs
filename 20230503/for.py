# Cerinta: Afiseaza-mi primele n patrate perfecte incepand de la un numar d.
n = int(input('Cate patrate doresti? '))
d = int(input('De unde sa incep? '))

for i in range(d, d + n):
    a = i * i
    print(f'patratul lui {i} este {a}')


exit()

# break
# for i in range(20):
#     if i == 5:
#         break
#     print(i)

numere = [25, 11, 13, 20, 49]
# for i in numere:
#     if i % 2 == 0:
#         break
#
#     print(i)

for i in numere:
    if i % 2 == 0:
        continue

    print(i)

# echivalent cu
for i in numere:
    if i % 2 == 1:
        print(i)

# n = int(input())
#
# for i in range(1, n, 3):
#     print(i)

lista_mea = [10, 13, 53, 2, 42, 54]
# lista_mea.pop()
# lista_mea.append(-23)

# varianta 1
# for element in lista_mea:
#     print(element)

# varianta 2
# for i in range(len(lista_mea)):
#     print(f'{i}: {lista_mea[i]}')

# for i in range(0, len(lista_mea), 2):
#     print(f'{i}: {lista_mea[i]}')
