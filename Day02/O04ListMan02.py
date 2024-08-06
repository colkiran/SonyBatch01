
print('append'.center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# append - can add one value at a time
l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

#from the result print 10, 11, 12
print(l1[8][1:4])

print('extend'.center(60, "-"))
# extend - can add more than one value like a list
l2 = [2, 4, 6, 8, 10]
print(f"l2 :{l2}")

l2.extend([12, 14, 16])
print(f"l2 :{l2}")

l2.extend([18])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = list(range(1, 10, 2))
print(f"l1 :{l1}")

l1.insert(1, 2)
l1.insert(3, 4)
l1.insert(5, 6)
l1.insert(7, 8)
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 3, 2, 2, 2 ,2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1 ]
print(f"l1 :{l1}")

print('-' * 60)

l1.remove(3)
l1.remove(3)

print(f"l1 :{l1}")

# for i in l1:
#     if i == 1:
#         l1.remove(1)

while(1 in l1):
    l1.remove(1)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = [1, 2, 3, 4, 5]

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()      # removes the last element from the list
print(f"res :{res}")

# res = l1.pop(6)
# print(f"res :{res}")

print("l1 :{l1}")

print('clear'.center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
