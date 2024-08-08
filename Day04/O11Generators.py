
def fun():
    x = 1
    print("apples from ooty...")
    yield x
    x += 9
    print("oranges from kanpur....")
    yield x
    x += 10
    print("Grapes from hubli.....")
    yield x

obj = fun()
print(type(obj))

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
# print(obj.__next__())

print("-" * 60)

def fun1():
    for i in range(2, 11, 2):
        yield i

obj = fun1()

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())



