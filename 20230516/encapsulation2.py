class Masina:
    __culoare = 'gri'

    @property
    def culoare(self):
        return self.__culoare

    @culoare.getter
    def culoare(self):
        print('Returnam culoarea')
        return self.__culoare

    @culoare.setter
    def culoare(self, culoare):
        print('Setam culoarea')
        if type(culoare) != str:
            raise TypeError('culoarea trebuie sa fie string')
        self.__culoare = culoare

    @culoare.deleter
    def culoare(self):
        print('Stergem culoarea')
        self.__culoare = 'gri'


m = Masina()

print(m.culoare)
m.culoare = 'rosu'
print(m.culoare)

del m.culoare

print(m.culoare)

di = {}
del di['test']
