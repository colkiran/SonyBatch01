
"""
1. arithmetic
2. augmentor
3. comparison
4. logical
5. bitwise
6. ternary
"""

print("Arithmetic Operators".center(60, "-"))
print(f"Sum  10 + 3 = {10 + 3}")
print(f"Diff 10 - 3 = {10 - 3}")
print(f"Prod 10 * 3 = {10 * 3}")
print(f"Div  10 / 3 = {10 / 3}")
print(f"Flr_div  10 // 3 = {10 // 3}")
print(f"mod 10 % 3 = {10 % 3}")
print(f"power 10 ** 3 :{10 ** 3}")

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=

x = 5
print(f"x :{x}")

x *= 3
print(f"x :{x}")

x /= 5
print(f"x :{x}")

print("Comparison".center(60, "-"))
# ==, !=, >, <, >=, <=
a = 10
b = 15

print(f"a == b :{a == b}")
print(f"a > b  :{a > b}")
print(f"a < b  :{a < b}")
print(f"a != b :{a != b}")

print("logical".center(60, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print("-" * 60)

print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 2 == 2 :{1 == 2 or 2 == 2}")
print("-" * 60)

print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 2 or 2 == 2) :{not(1 == 2 or 2 == 2)}")

print("Bitwise".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"5 >> 1 :{5 >> 1}")

print('ternary'.center(60, "-"))
age = 18
print("Eligible" if age > 17 else "Not Eligible")
