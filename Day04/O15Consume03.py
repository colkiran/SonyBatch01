
import sys

# print(sys.path)

sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

print("-" * 60)
import gurgaon.mymodule as m
from gurgaon.mymodule import greet, Employee

print(f"runs :{m.runs}")

print(f"sports :{m.sports}")

greet("Rohit")

print("-" * 60)
emp1 = Employee('Tina',    25000)
print(emp1)