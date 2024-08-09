"""
self - will have the name of the object that called the method

ply1.get_details()

def get_details(self)       # self = ply1
    print(self.name)        # ply1.name
    print (self.age)        # ply1.age

ply1 = __dict__ = {'name': 'Sachin', 'age': 35}


"""

class Player:

    def __init__(self, name, age):
        self.age = age
        self.name = name
        print("Player Initialized......")

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 60)

ply2 = Player("Sourav", 35)
ply2.get_details()

print("-" * 60)  
ply2.runs = 150

print("ply2 :", ply2.__dict__)

print("-" * 60)

print("ply1 :", ply1.__dict__)
