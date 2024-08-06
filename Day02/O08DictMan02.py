
print("get".center(60, "-"))
player = {'name': 'Sourav', 'age': 34, 'runs': 80,
          'oppn': 'SA'}
print(f"player :{player}")

print(f"name :{player.get('name')}")
print(f"runs :{player.get('run', 'Invalid Key please enter a valid Key......')}")

print("keys".center(60, "-"))
player = {"Name":'lionel Messi', 'age': 36, 'goals': 55, 'country': 'argentia',
          'club': 'Miami FC', 'ballandor': 8 }
print(f'player :{player}')

kys = player.keys()
print(f"Keys :{kys}")

print("-" * 60)
for k in player.keys():
    print(k, "=>", player[k])

print('values'.center(60, "-"))
player = {"Name":'lionel Messi', 'age': 36, 'goals': 55, 'country': 'argentia',
          'club': 'Miami FC', 'ballandor': 8 }
print(f'player :{player}')

vl = player.values()
print(f"values :{vl}")

print("items".center(60, "-"))
# items = keys + values

player = {"Name":'lionel Messi', 'age': 36, 'goals': 55, 'country': 'argentia',
          'club': 'Miami FC', 'ballandor': 8 }
print(f'player :{player}')

print("-" * 60)
for k, v in player.items():
    print(k, "=>", v)

print("-" * 60)
emp = {
    'emp1':{'ename': 'Jack', 'age': 34, 'desig': 'Tl', 'dept': 'finance', 'salary': 85000},
    'emp2':{'ename': 'Jenny', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 23000},
    'emp3':{'ename': 'Kevin', 'age': 38, 'desig': 'MGR', 'dept': 'IT', 'salary': 185000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)