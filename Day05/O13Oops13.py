
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        self.__price = val

    def del_price(self):
        self.__price = 0

    price = property(get_price, set_price, del_price)


coke = Product(50)
print(coke.price)               # getter

coke.price = 85                 # setter

print(coke.price)

del coke.price

print(coke.price)

