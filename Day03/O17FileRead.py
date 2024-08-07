
FL = open("data.txt", "r")       # defualt mode is read mode

st = FL.read(100)
print(st)

FL.close()