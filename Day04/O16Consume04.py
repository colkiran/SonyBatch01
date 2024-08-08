

import sys

for pth in sys.path:
    print(pth)

print("-" * 60)
import gurgaon.mymodule as m
from gurgaon.mymodule import greet, Employee

print(f"runs :{m.runs}")

print(f"sports :{m.sports}")

print("-" * 60)

greet("Sourav")

print("-" * 60)
emp1 = Employee('Peter', 75000)
print(emp1)