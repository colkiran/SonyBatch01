
import mypackage.mymodule as m
from mypackage.mymodule import greet, Employee

print(f"runs :{m.runs}")

print(f"sports :{m.sports}")

greet("Rohit")

emp1 = Employee('Slater', 53000)
print(emp1)