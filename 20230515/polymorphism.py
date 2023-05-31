class Tara:
    def limba(self):
        print('Nu am limba')


class Romania(Tara):
    def limba(self):
        print('Romana')


class SUA(Tara):
    def limba(self):
        print('Engleza')


class Narnia(Tara):
    pass


tari = [Romania(), SUA(), SUA(), Tara(), Narnia()]

for tara in tari:
    tara.limba()


def suma(a, b, c=0):
    if isinstance(a, tuple) and isinstance(b, tuple):
        return a[0] + b[0], a[1] + b[1]

    return a + b


print(suma(10, 3, 2))
print(suma(10, 4))

a = (1, 4)
b = (4, 5)
print(suma(a, b))
