# def patrat(a):
#     return a * a
#
#
# def intreg(a):
#     return int(a)
#
#
# def dublu(a):
#     return 2 * a


# actions = {
#     'patrat': lambda a: a * a,
#     'intreg': lambda a: int(a),
#     'dublu': lambda a: 2 * a
# }
#
# comanda = input('da-mi o comanda ')
# numar = float(input('da-mi un numar '))
#
# print(actions[comanda](numar))

# def produs(a, b):
#     return a * b
# produs = lambda a, b: a * b
#
# print(produs(10, 11))


arr = ['cal', 'rinocer', 'avion']


def sort_key(s):
    return len(s)


print(sorted(arr, key=lambda s: len(s)))
