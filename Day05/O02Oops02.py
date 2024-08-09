
class Player:

    def __init__(self):
        print("Player Initialized.......")

    def get_runs(self):
        print("Runs scored.....")

    # destructor
    def __del__(self):
        print("destructor called......")

sachin = Player()
sourav = Player()

sachin.__init__()
print('-' * 60)

sachin.get_runs()
sourav.get_runs()

# deleting an object and calling the destructor
del sachin
sourav.get_runs()
sourav.get_runs()
sourav.get_runs()

print("Hello World")