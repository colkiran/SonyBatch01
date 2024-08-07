
values = [10, 20, 30]
print(f"l1 :{values}")
print(type(values))

print("-" * 60)
a, b, c = values            # unpacking
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")
# unpack
# a variable prefixed with * can accept more than one value and store it like a tuple
a, b, *c = values
print(a, b, c, sep=", ")
print("-" * 60)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

print("-" * 60)
lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(f"len(lst3) :{len(lst3)}")

print("-" * 60)
lst4 = [*lst1, *lst2]
print(f"lst4 :{lst4}")
print(f"len(lst4) :{len(lst4)}")

print("-" * 60)
elements = ['a', 'b', 'c', 'd', 'e']
print(f"elements :{elements}")

print("-" * 60)
print(list(enumerate(elements)))

print("-" * 60)
for letter in enumerate(elements):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(elements):
    print(letter[0], letter[1])

print("-" * 60)
lst1 = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12]]
for elem in enumerate(lst1):
    print(elem[0])
    for ele1 in enumerate(elem[1]):
        print("\t\t",ele1[0], "\t\t", ele1[1])
