
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


    @classmethod
    def CreatePlayer(cls, fnm, lnm, age):
        print("Factory")
        return cls(f"{fnm} {lnm}", age)         # this will the constructor


ply1 = Player('Rohit Sharma', 35)
ply1.get_details()

print("-" * 60)

ply2 = Player.CreatePlayer("Virat", "Kholi", 36)
ply2.get_details()

