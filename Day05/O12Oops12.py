
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError ('Value cannot be less than zero (0)')
        else:
            self.__price = val

    def del_price(self):
        self.__price = 0

import sys

try:
    pepsi = Product(45)

    print(pepsi.get_price())

    pepsi.set_price(50)

    print(pepsi.get_price())

    pepsi.del_price()

    print(pepsi.get_price())


except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

