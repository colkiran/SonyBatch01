
FL = open("sample.txt", "w+")

st = input("Enter some content :")
FL.write(st)

FL.seek(0, 0)
txt = FL.readlines()
print(txt)

FL.close()