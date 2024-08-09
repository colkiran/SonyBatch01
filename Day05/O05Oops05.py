
class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_Details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Virat", 34)
ply1.get_Details()

print("-" * 60)
ply2 = Player("Rohit", 33)
ply2.get_Details()

print("-" * 60)
Player.team = "India"

print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
Player.team = "MI"

print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
ply1.team = "RCB"
print(f"ply1   :{ply1.team}")

print(f"Player :{Player.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
print(f"Player :{Player.__dict__}")