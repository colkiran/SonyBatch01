
gname = "Sachin Tendulkar"

sports = ['cricket', 'football', 'tennis', 'basket ball', 'swimming']

runs = {'test': 20500, 'odi': 18900, 't20': 2500}

def greet(gnm):
    print(f"Greetings {gnm}, welcome to the event.....")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

# print(f"__name__ :{__name__}")

if __name__ == '__main__':

    greet(gname)

    print("-" * 60)

    emp1 = Employee("Kevin", 65000)
    print(emp1)