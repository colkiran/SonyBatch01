
glbX = 100

def fun(x):                 # x is a local variable
    global glbX             # do not assign any value in this line
    y = "hello world"       # y is a local variable
    print(f"x :{x}")
    print(f"y :{y}")

    glbX = 500
    print(f"glbX inside :{glbX}")


print(f"glbX before :{glbX}")

fun(10)

print(f"glbX after :{glbX}")
