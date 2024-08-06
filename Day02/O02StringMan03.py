
print("Welcome %s, what a %s player" % ("Sachin", "class"))
print("Welcome %s, what a %s player with a rating %.2f" % ("Sachin", "class", 9.34567))

print("-" * 60)
gname= "Sachin"
adj = "class"
rating = "9.3456"
print(f"Welcome {gname}, what a {adj} player with a rating {rating}")

print("-" * 60)
# python string formatting
print("Welcome {gname}, what a {adj} player with a rating {rating}".format(gname="Sachin", adj="superb", rating=9.6798))

print("Welcome {}, what a {} player with a rating {:.2f}".format("Sachin", "superb", 9.6798))

print("-" * 60)
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("{num} {num} {num}".format(num=36))
print("{num} {num:f} {num:b}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36434767234234))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
from math import pi

print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
# alignment
print("{val:15} Tendulkar".format(val = "Sachin"))
print("{val:15} Tendulkar".format(val = 501))
print("{val:015} Tendulkar".format(val = 501))

print("{val:>15} Tendulkar".format(val = "Sachin"))      # right alignment
print("{val:^15} Tendulkar".format(val = "Sachin"))      # center alignment
print("{val:<15} Tendulkar".format(val = "Sachin"))      # left alignment

print('sachin'.center(60, "-"))
print("{val:-^60}".format(val = "Sachin"))




