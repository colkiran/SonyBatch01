
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'Sachin', 'age': 32, 'runs': 130, 'oppn':  "WI", 'venue': 'Sabina Park'}
print(f"d2 :{d2}")
print(type(d2))
print("-" * 60)

d3 = dict([('name', 'rahul'), ('age', 30), ('runs', 87), ('oppn', 'SA')])
print(f"d3 :{d3}")
print(type(d3))
print("-" * 60)

d4 = dict(name='Virat', age=35, runs=120, oppn="pak")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 34, 'runs': 145, 'oppn': 'Aus'}
print(f"player :{player}")

print("-" * 60)
# read

print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate

for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update

player['name'] = "Tendulkar"
player['oppn'] = "Nzl"

player['year'] = 2003
player['venue'] = "Auckland"

print(f'player :{player}')

print("-" * 60)
# delete

print(f"player :{player}")
del player['age']
del player['oppn']
print(f"player :{player}")

print("-" * 60)
print(dir(player))

