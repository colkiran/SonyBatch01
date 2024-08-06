
print("fromkeys".center(60,"-"))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cites :{cities}")

res = dict.fromkeys(cities)       # values are none
print(f"res :{res}")

res1 = dict.fromkeys(cities, 24)
print(f"res1 :{res1}")

print("setdefault".center(60, "-"))

emp1 = {'ename': 'Jack', 'age': 34, 'desig': 'Tl', 'dept': 'finance', 'salary': 85000}
print(f"emp1 :{emp1}")

emp1.setdefault('ename', 'Peter')
emp1.setdefault('dept', "Procurement")

emp1['gender'] = "Male"
emp1['location'] = "Mumbai"

print('-' * 60)
print(f"emp1 :{emp1}")

print('pop'.center(60, "-"))
emp1 = {'ename': 'Jack', 'age': 34, 'desig': 'Tl', 'dept': 'finance', 'salary': 85000, 'gender': 'Male', 'location': 'Mumbai'}

print(f"emp1 :{emp1}")

res = emp1.pop('age')
print(f"res :{res}")

res = emp1.pop('dept')
print(f"res :{res}")

# res = emp1.pop('age')
# print(f"res :{res}")

print(f"emp1 :{emp1}")


print("popitem".center(60, "-"))

emp1 = {'ename': 'Jack', 'age': 34, 'desig': 'Tl', 'dept': 'finance', 'salary': 85000, 'gender': 'Male', 'location': 'Mumbai'}

print(f"emp1 :{emp1}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

print("update".center(60, "-"))

emp2 = {'ename': 'Jenny', 'age': 28, 'dept': 'MKT', 'salary': 23000}

emp3 = {'ename': 'Kevin', 'age': 38, 'desig': 'MGR', 'dept': 'IT'}
print("-" * 60)
print(f"emp2 :{emp2}")
print("-" * 60)
print(f"emp3 :{emp3}")
emp2.update(emp3)
print("-" * 60)

print(f"emp2 :{emp2}")
print("-" * 60)
