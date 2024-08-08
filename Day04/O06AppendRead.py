
FL = open("sample.txt", "ab+")

FL.seek(100, 2)
# st = input("Enter the  contents :")
FL.write(b"hello world")

FL.seek(0, 0)
txt = FL.read()
print(txt)

FL.close()