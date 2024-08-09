class arith:
    def __init__(self,a):
        self.a = a
        #self.b = b
    def  __add__(self, other):
        return self.a + other.a
    def __sub__(self, other):
        return self.a - other.a
    def __mul__(self, other):
        return self.a * other.a
    def __truediv__(self, other):
        return self.a / other.a
    def __floordiv__(self, other):
        return self.a // other.a


ar1 = arith(10)
ar2 = arith(5)


print(ar1+ar2)
print(ar1-ar2)
print(ar1*ar2)
print(ar1/ar2)