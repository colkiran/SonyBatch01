from collections import  namedtuple

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("arithCalc", "s d p q")
    arithcalc = nmdTpl(s= sum, d=diff, p=prod, q = quot)
    return arithcalc

res = arithmeticCalc(20,8)
print(res)

print(f"Sum  :{res.s}")
print(f"Diff :{res.d}")
print(f"Prod :{res.p}")
print(f"quot :{res.q}")

