
print('index'.center(60, "-"))
l1 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 3, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1 ]
print(f"l1 :{l1}")

idx = l1.index(3)
print(f"index :{idx}")

idx = l1.index(3, l1.index(3) + 1)
print(f"index :{idx}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2

l2 = l1         # shallow copy - copy the address along with values

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
print("=" * 60)

l3 = [5, 10, 15, 20, 25]
print(f"l3 before :{l3}")

# copy the values of l3 to l4
l4 = l3.copy()
print(f"before :{l4}")

l4.extend([30, 35, 40, 45])

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
print("=" * 60)

l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]
print(f"l5 before :{l5}")

# copy the list l5 to l6
l6 = l5.copy()
print(F'l6 before :{l6}')

l6[3].extend([60, 70, 80])

print(f'l5 after :{l5}')
print(f'l6 after :{l6}')

print("=" * 60)
print("=" * 60)

l7 = [2, 4, [1, 2, 3, 4, 5], 6, 8, 10]
print(F"l7 before :{l7}")

# copy the elements of l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[2].extend([6, 7, 8, 9])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")
