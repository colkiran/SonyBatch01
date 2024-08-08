
lst1 = [x for x in range(1, 11)]            # comprehension
print(f"lst1 :{lst1}")
print(type(lst1))
print("-" * 60)

lst1 = (x for x in range(1, 11))            # generator
print(f"lst1 :{lst1}")
print(type(lst1))
print("-" * 60)

s1 = sum([x ** 2 for x in range(1, 11)])
print(f"Result accomplished using comprehension :{s1}")
print("-" * 60)

s2 = sum((x ** 2 for x in range(1, 11)))
print(f"Result accomplished using generators :{s2}")
print("-" * 60)

from sys import getsizeof

t1 = [x ** 2 for x in range(1, 10000)]
print(f"Compreshension generated list :{getsizeof(t1)}")
print("-" * 60)

t2 = (x ** 2 for x in range(1, 10000))
print(f"Generator generated list :{getsizeof(t2)}")
print("-" * 60)
