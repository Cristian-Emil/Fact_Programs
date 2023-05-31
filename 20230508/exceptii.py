cuvant = 'arbore'
numar = '10'
valoare = 0
dictionar = {
    'a': 10
}

# try:
#     print(dictionar['b'])
#     print(cuvant + ' ' + numar)
#     valoare = 1
# except TypeError as te:
#     print('Eroare de tip.')
# # except KeyError as ke:
# #     print(f'Key ul {ke} este inexistent')
# # except Exception as e:
# #     print(e)
# else:
#     print('Nu a aparut nicio eroare')
# finally:
#     print('Se executa mereu')
#
# print(valoare)
# print('Gata')


def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        print('This is always executed')

    print('Aici')


# divide(10, 3)


def produs_pozitive(x, y):
    if x < 0 or y < 0:
        raise Exception('numerele trebuie sa fie pozitive')

    return x * y


try:
    rez = produs_pozitive(4, -3)
    print(rez)
except Exception as e:
    print(e)
    print('Nu mi-au palcut numerele')
