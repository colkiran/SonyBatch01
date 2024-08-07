
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun


KanGrt = outerFun("Namaskara")

KanGrtTgr = KanGrt("tiger")

KanGrtTgr("Prabhakar")




"""
outerFun("Welcome")("----->")("Sachin")
print("-" * 60)

engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

engGrtSngArw = engGrt("------>")
tmlGrtSngArw = tmlGrt("------>")
engGrtDblArw = engGrt("=====>>")
tmlGrtDblArw = tmlGrt("=====>>")

engGrtSngArw("Rahul")
engGrtDblArw("Sachin")
tmlGrtSngArw("Ashwin")
tmlGrtDblArw("Dhoni")

"""