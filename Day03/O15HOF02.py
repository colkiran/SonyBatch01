
def callMe():
    print("apples from ooty......")

def fun(fnc):
    print("Hi......")
    fnc()
    print("Hello......")
    print("-" * 60)

    def defineMe():
        print("Oranges from Kanpur....")

    return defineMe

def CallBack(fnc):
    print("Mera Bharath Mahan.......")
    fnc()
    print('India is great......')


CallBack(fun(callMe))
