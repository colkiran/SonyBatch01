
class Animal:

    def __init__(self):
        print('Animal Ctor.....')
        self.a = 100

    def eat(self):
        print("Animals eat.......")


    def fun(self):
        print("Animal Classes fun method....")


class Person:

    def __init__(self):
        print('Person Ctor.....')
        self.p = 20

    def talk(self):
        print("Person Talks.....")

    def fun(self):
        print("Person Classes fun method....")



class Girl(Animal, Person):

    def __init__(self):
        super().__init__()              # parent
        Person.__init__(self)           # person
        print('Girl Ctor....')
        self.g = 30


    def walk(self):
        print("Girls Walk.......")





tina = Girl()
tina.eat()
tina.talk()
tina.walk()

print("-" * 60)

tina.fun()

print("-" * 60)
print(tina.__dict__)