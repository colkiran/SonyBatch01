
def outerFun(gname):

    def innerFun():

        print(f"Greetings {gname}, Welcome to the event......")

    return innerFun

inrRef = outerFun("Sachin")
print("hello")

print("world")

# we have lost the scope of outerFun - but still I am access outerFun variables
inrRef()        # calls the innerFun

print("-" * 60)

outerFun("Rahul")()         # calls the innerFun