
# any varaible declared inside the function cannot be accessed outside the function

def fun(x):

    y = "hello world"
    print(f"y inside :{y}")
    print(f"x inside :{x}")

fun(15)

# print(f"x :{x}")
# print(f"y :{y}")