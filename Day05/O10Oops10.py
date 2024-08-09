
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'Angular', "React" ]

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val

        

emp1 = Employee('Peter', 75000)
print(emp1)

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)

tch = emp1[3]
print(f"tch :{tch}")

print("-" * 60)

emp1.append("Python")
print([emp for emp in emp1])

print("-" * 60)

emp1[2] = "JSP"
print([emp for emp in emp1])

