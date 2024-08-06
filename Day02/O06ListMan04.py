"""
sort - this will sort the original list
sorted - this will take a copy of the list and sort it
"""
print("sort".center(60, "-"))
l1 = [8, 6, 10, 1, 9, 4, 2, 5, 7, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 60)

l1 = [8, 'zebra', 'apple', 6, 'violet', 'blue', 10, 'white', 'green', 1, 'yellow', 'maroon', 9, 'dog', 'cat', 4, 'hen', 'egg', 2, 5, 7, 3, 190, 1024, 28, 241, 2110]
print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")
#res.index(1)
'''
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        break
'''
print("-" * 60)
print(res[:12] + sorted(res[12:]))

print("-" * 60)

cities = ['vishakapatnam', 'bangalore', 'pune', 'thiruvananthapuram', 'mysore', 'hyderabad', 'ooty', 'chennai', 'madurai', 'delhi', 'mumbai']

print(f"cities :{cities}")

print("-" * 60)
asc = sorted(cities, key=len)
print(asc)

print("-" * 60)
desc = sorted(cities, key=len, reverse=True)
print(desc)


print("reverse".center(60, "-"))

l1 = [8, 6, 10, 1, 9, 4, 2, 5, 7, 3]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")