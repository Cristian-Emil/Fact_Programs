class Carbonara:
    oua = 2
    bacon_gr = 100
    spaghetti_gr = 90

    def taie_bacon(self):
        print(f'Am taiat {self.bacon_gr} g bacon')

    def amesteca(self):
        print('Am amestecat ingredientele')


carbonara1 = Carbonara()

# print('Portie 1 carbonara')
# print(carbonara1.oua)
# print(carbonara1.bacon_gr)
# print(carbonara1.spaghetti_gr)
# print(carbonara1.condiemnte)
# carbonara1.taie_bacon()
#
# carbonara2 = Carbonara()
# carbonara2.oua = 3
# carbonara2.spaghetti_gr = 70
#
# print('Portie 2 carboanra')
# print(carbonara2.oua)
# print(carbonara2.bacon_gr)
# print(carbonara2.spaghetti_gr)
# carbonara2.taie_bacon()


class Triunghi:
    a = 10
    b = 20
    c = 18

    def perimetrul(self, factor=1):
        return factor * (self.a + self.b + self.c)


# t1 = Triunghi()
# print(t1.perimetrul())
#
# t2 = Triunghi()
# t2.b = 22
# print(t2.perimetrul())
#
# print(t1.b)
# print(t2.b)
#
# print(t2.perimetrul(2))

class Car:
    make = 'BMW'
    model = None
    year = 1900
    color = None

    def __init__(self, make, year=1990):
        self.make = make
        if year >= 1900:
            self.year = year
        else:
            raise Exception('Nu te cred')


    def accelerare(self):
        print('Am crescut viteza!')


car = Car('Audi', 2000)
# car = Car()
print(car.make)
print(car.year)

car.make = 'Renault'
print(Car.make)


car2 = Car('Seat', 2010)
print(car2.make)
print(car.make)
print(Car.make)

# print(car.__dir__())
