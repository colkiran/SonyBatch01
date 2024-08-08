
FL = open("myfile.txt", "r+")

st = FL.readline()
print(st)

FL.seek(25, 0)

txt = input("Enter the contents of the file :")
FL.write(txt)

FL.close()