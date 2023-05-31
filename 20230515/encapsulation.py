class Masina:
    __culoare = 'gri'

    def arata_culoarea(self):
        return self.__culoare

    def seteaza_culoarea(self, culoare):
        if type(culoare) != str:
            raise TypeError('culoarea trebuie sa fie string')
        self.__culoare = culoare


masina = Masina()
# masina.__culoare = 31
masina.seteaza_culoarea('albastru')
# print(masina.__culoare)
print(masina.arata_culoarea())

# print(masina.__dict__)
# print(masina.__dir__())
