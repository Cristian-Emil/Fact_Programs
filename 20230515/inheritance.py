class Chef:
    def __init__(self, exp):
        self.experienta = exp

    def fa_salata(self):
        print('salata')

    def fa_cartofi(self):
        print('cartofi')


class JapaneseChef(Chef):
    def __init__(self, exp, nume):
        super().__init__(exp)
        self.nume = nume
        print(f'Salut, sunt un chef din Japonia. Ma numesc {nume}')

    def fa_sushi(self):
        print('sushi')


class ItalianChef(Chef):
    def fa_pizza(self):
        print('pizza')


print('*' * 10 + ' chef 1 ' + '*' * 10)
chef = Chef(10)
chef.fa_salata()
chef.fa_cartofi()
print(str(chef.experienta) + ' ani')

print('*' * 10 + ' chef 2 ' + '*' * 10)
jchef = JapaneseChef(4, 'Marcel')
jchef.fa_sushi()
jchef.fa_salata()
jchef.fa_cartofi()
print(str(jchef.experienta) + ' ani')

# print('*' * 10 + ' chef 3 ' + '*' * 10)
# ichef = ItalianChef(6)
# ichef.fa_pizza()
# ichef.fa_salata()
# ichef.fa_cartofi()
# print(str(ichef.experienta) + ' ani')

class A:
    def f(self):
        print('Clasa A::f')
    def g(self):
        print('Clasa A::g')


class B(A):
    def f(self):
        print('Clasa B::f')


class C(B):
    def f(self):
        print('Clasa C::f')


c = C()
c.f()
c.g()