def add(x, y):
    return x + y

# res = add(34,  89)
# print(res)

a = add
print(a(59, 47))

k = lambda x, y :x + y
print( k(59, 47))

# print("-" * 60)
# map, filter and reduce

print("map".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

print("-" * 60)
print("-" * 60)

months = ['dec', 'aug', 'nov', 'jan', 'sep', 'apr', 'oct' , 'mar', 'may', 'jul', 'feb', 'jun']
print(f"unsorted months :{months}")

from calendar import month_abbr
print(f"Month Names :{list(month_abbr)}")

res = sorted(months, key=list(map(lambda mth : mth.lower(), list(month_abbr))).index )
print(res)

print('filters'.center(60,"-"))
l1 = list(range(1, 31))
print(f"l1 :{l1}")

res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("reduce".center(60, "-"))
l1 = [8, 5, 9, 7, 6, 10, 4, 3]
print(f"l1 :{l1}")

from functools import reduce

res = reduce(lambda x, y: x if x < y else y, l1)
print(res)

res  = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
