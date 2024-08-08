
lst1 = ['a', 'b', 'c', 'd', 'e']
print(f"lst1 :{lst1}")

# print(dir(lst1))

iterObj = lst1.__iter__()
# iterObj = iter(lst1)

print("-" * 60)
print(dir(iterObj))

print("-" * 60)
elem1 = iterObj.__next__()
print(f"elem1 :{elem1}")

print("-" * 60)
elem1 = iterObj.__next__()
print(f"elem1 :{elem1}")


elem1 = iterObj.__next__()
print(f"elem1 :{elem1}")

print("-" * 60)
elem1 = iterObj.__next__()
print(f"elem1 :{elem1}")

print("-" * 60)
elem1 = iterObj.__next__()
print(f"elem1 :{elem1}")

# print("-" * 60)
# elem1 = iterObj.__next__()
# print(f"elem1 :{elem1}")

