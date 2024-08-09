
class Player:           # pascal casing

    def get_runs(self):
        print("Runs scored.....")

ply1 = Player()             # calls the constructor
print(type(ply1))
ply1.get_runs()

print("-" * 60)

print(isinstance(ply1, Player))
print(isinstance(ply1, object))


