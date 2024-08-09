

class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    @price.deleter
    def price(self):
        self.__price = 0




coke = Product(50)
print(coke.price)               # getter

coke.price = 85                 # setter

print(coke.price)

del coke.price

print(coke.price)

