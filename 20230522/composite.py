from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        raise NotImplementedError


class Box(Component):
    def __init__(self):
        self.__components = []

    def operation(self):
        print('Ai deschis cutia')

        for c in self.__components:
            c.operation()

    def add(self, component: Component):
        if component not in self.__components:
            self.__components.append(component)

    def remove(self, component: Component):
        if component in self.__components:
            self.__components.remove(component)


class Product(Component):
    def __init__(self, name=''):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    def operation(self):
        print(f'Pordus: {self.__name}')


big_box = Box()

toy = Product('jucarie darguta')
little_box = Box()

screwdriver = Product('surubelnita')
key = Product('cheie')
little_box.add(screwdriver)
little_box.add(key)

# little_box.operation()

big_box.add(toy)
big_box.add(little_box)

big_box.operation()
