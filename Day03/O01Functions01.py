
def greet():
    print("Greetings Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings {gname}, Welcome to the event........")

# city is called default arg, and gname is called non default arg
# all non default arg should be declared before default arg
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings {gname} from {city}, Welcome to the event......")

greet()
print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")
print("-" * 60)

greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
def admsn(sname, dob, gender, qlf, conno, mailid, adr, city, idprf):
    print(f"Name :{sname}")
    print(f"DOB  :{dob}")
    print(f"Gender :{gender}")
    print(f"Qualification :{qlf}")
    print(f"Contact no. :{conno}")
    print(f"Email ID :{mailid}")
    print(f"Address :{adr}")
    print(f"City :{city}")
    print(f"ID Proof :{idprf}")

# named arguments
admsn(city = "Hyderabad", dob="16/04/1998", idprf="Adhar Card", sname = "Keneddy", conno="82374892", mailid="Ken@gmail.com", gender="male", qlf="Mtech", adr="8th main, 10th cross, Gachibowli")

print("-" * 60)
# variable length args - *args, **kwargs

def prodAll(*numbers):
    print(*numbers)
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod


res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extractDetails(**details):
    print(details)
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name="Mike Tyson", sport="Boxing", age=56, achievements="34 knockouts")

print("-" * 60)

def multiplyME(x, y):
    return x * y

a = 5
b = 37
print(f"The product of {a} and {b} is :{multiplyME(a, b)}")

# recursive calls - return
# 1. factorial of a number , 2. fibanocci series

print("-" * 60)

def fun():
    "This is a doc string"
    # this is a comment
    print("hello world")

fun()

print(fun.__doc__)

print("-" * 60)
def fun1(x, y):
    """
        fun1(x, y)
        ----------

        1. if x and y are integers then the result would be the sum of the numbers
        2. if x and y are strings then the result would be the concatenation of the strings
        3. if x and y are of different data type then it will throw an error
    """
    return  x + y

fun1(10, 30)
fun1("Hello ", "world")

print("-" * 60)
help(fun1)
