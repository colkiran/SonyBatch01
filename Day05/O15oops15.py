
class Animal:

    def __init__(self):
        print("Animal Ctor")
        self.a = 10

    def eat(self):
        print("Animals eat.......")

class Bird(Animal):

    def fly(self):
        print("Birds Fly.....")


class Fish(Animal):

    def swim(self):
        print("Fishes Swim......")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)

print(cuckoo.__dict__)
print(dolphin.__dict__)