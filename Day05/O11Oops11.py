
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'Angular', "React"]

    def __str__(self):
        return self.__name + " - " + " ".join([str(st) for st in self.tech])


emp1 = Employee("Bernad")
print(emp1)

print("-" * 60)

print(emp1.__dict__)

print("-" * 60)

emp1._Employee__name = "Alwin"

print(emp1.__dict__)

print("-" * 60)

print(emp1)