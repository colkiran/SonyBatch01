
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

engGrt = outerFun("Hello")
tmlGrt = outerFun("Vanakam")


engGrt("Sachin")
engGrt("Mike Tyson")
engGrt("Beckam")

tmlGrt("Natraj")