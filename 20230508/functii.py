def salutare(prenume, nume='Pop', varsta=25):
    if not nume == '':
        print(f'Salut, {nume} {prenume}!')
    else:
        print(f'Salut, {prenume}!')

    print(f'Varsta ta este de {varsta} ani.')


# salutare('Adi', 'Moldovan', 10)
# salutare('Maria')
#
# nume = 'Popescu'
# prenume = 'Denis'
# salutare(prenume, nume)

def afiseaza_ptratul(x=1):
    print(f'Patratul lui {x} este {x * x}')


# afiseaza_ptratul(10)
# afiseaza_ptratul()

def salutare_return(prenume, nume='Pop'):
    if not nume == '':
        return f'Salut, {nume} {prenume}!'
    else:
        print(f'Salut, {prenume}!')

    print('Cum ajung aici?')


# rezultat = salutare_return('Mihai', '')
# print(rezultat)
# print(type(rezultat))


factor = 3
# print(factor)


def f(x):
    global factor
    factor = 10
    produs = factor * x
    return produs


produs = 15

# print(f(10))
# print(produs)
# print(factor)


# def add(a, b):
#     return 2 * a + b
#
#
# print(add(b=10, a=2))
# print(type(add))

cifre_control = reversed([2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9])
cnp = 198132306002
suma = 0

for i in cifre_control:
    suma += i * (cnp % 10)
    cnp //= 10

print(suma % 11)
