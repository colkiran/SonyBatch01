
l1 = list()
print(f'l1 :{l1}')
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.0, 8.2, 9.5, 10+2j, 11-3j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

l1 = list(range(1, 11))
print(f"l1 :{l1}")

# Read
print(f"l1[2] :{l1[2]}")
print(f"l1[5] :{l1[5]}")
print(f"l1[-1] :{l1[-1]}")

print("-" * 60)
for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("-" * 60)
# update = modify, insert new values
print(f"l1 :{l1}")

l1[2] = 300
l1[-2] = 900

l1[5] = "new elem"

print(f"l1 :{l1}")

print("-" * 60)
# delete
del l1[-3]
del l1[5]

print(f"l1 :{l1}")

print(dir(l1))
