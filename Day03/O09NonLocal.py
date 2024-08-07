
def outerFun():
    gname = "Sachin"
    def innerFun():
        nonlocal  gname
        gname  = gname + " Tendulkar"

        print("Hello World")
        print(f"Greetings {gname}")


    innerFun()
    print(gname)

outerFun()
