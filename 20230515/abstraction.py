from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sunet(self):
        print('Sunet de animal')

    # def culoare(self):
    #     print('nu are culoare')

    @abstractmethod
    def culoare(self):
        raise NotImplementedError


class Caine(Animal):
    def sunet(self):
        super().sunet()
        print('Ham ham')

    def culoare(self):
        print('culoare maro')


class Pisica(Animal):
    def sunet(self):
        print('Miau miau')

    def culoare(self):
        print('culoarea alb')


# animal = Animal()
caine = Caine()
pisica = Pisica()

# animal.sunet()
caine.sunet()
caine.culoare()
print('*' * 20)
pisica.sunet()
pisica.culoare()


# class A:
#     def __init__(self, a, b, c):
#         self.param_a = a
#         self._param_b = b
#         self.__param_c = c
#
#     def afiseaza_c(self):
#         print(self.__param_c)
#
# class B(A):
#     def afiseaza_b(self):
#         print(self._param_b)
#
#     # def afiseaza_c(self):
#     #     print(self.__param_c)
#
# a = A(10, 20, 30)
# print(a.param_a)
# print(a._param_b)
# # print(a.__param_c)
# a.afiseaza_c()
#
# b = B(100, 200, 300)
# b.afiseaza_b()
# b.afiseaza_c()
