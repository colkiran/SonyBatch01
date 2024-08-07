
def fun(*args):
    return args

print(fun())
print(fun(1))
print(fun(1, 2))
print(fun(1, 2, 3))
print(fun(1, 2, 3, 4))


def sum(x, y):
    print(f"summing {x} and {y}")
    return x + y

def diff(x, y):
    print(f"find the difference of {x} and {y}")
    return x - y


print("-" * 60)

def outerFun(fnc):                  # HOF - Higher order functions
    # they are functions that take another function as argument or return a function as reference

    def innerFun(*args):
        print("Logging into a service,.....")
        print(fnc(*args))               # call back
        print("Logging out of the service....")
        print("-" * 60)

    return innerFun

sumlogger = outerFun(sum)
sumlogger(34, 76)