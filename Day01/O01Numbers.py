
a = 10
b = -10

print(f"a :{a}")
print(type(a))              # RTTI - Run Time Type Identification
print(f"b :{b}")
print(type(b))

b = 20
print(f"The sum of {a} and {b} is :{a + b}")
print("-" * 60)

c = 10.0
d = -10.0

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3

print(f'e :{e}')
print(type(e))
print(f'f :{f}')
print(type(f))

print("-" * 60)
g = 10 + 3j
h = 10 - 3j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))
print("-" * 60)

print(10, 8, 5, 2, 16, 9, 11, 14)
print(max(10, 8, 5, 2, 16, 9, 11, 14))
print(min(10, 8, 5, 2, 16, 9, 11, 14))

print("-" * 60)

x = 2 + 3.5
print(type(x))

x = 2
y = 3.5
z = x + y
print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("conversion".center(60, "-"))
x = 10
print(f"{type(x)}\t\t{x}")
print(f"{type(float(x))}\t\t{float(x)}")
print(f"{type(complex(x))}\t\t{complex(x)}")
print(f"{type(bool(x))}\t\t{bool(x)}")

print("Number System Coversion".center(60, "-"))
a = 100
print(bin(a))
print(hex(a))
print(oct(a))

print("Number System".center(60, "-"))
print(f"0b11 :{0b11}")      # binary        2 ** 2, 2 ** 1, 2 ** 0
print(f"0b101 :{0b101}")    # binary
print(f"0xa  :{0xa}")     # hexa
print(f"0xe  :{0xe}")
print(f"0o11 :{0o11}")      # octal
print(f"0o101 :{0o101}")