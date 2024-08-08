
FA = open("data.txt", "rb")

pos = FA.seek(50, 0)
print(f"position :{pos}")

pos = FA.seek(85, 1)
print(f"position :{pos}")

pos = FA.seek(0, 2)
print(f"position :{pos}")

pos = FA.seek(100, 2)
print(f"position :{pos}")

pos = FA.seek(-100, 2)
print(f"position :{pos}")

pos = FA.seek(-10, 0)
print(f"position :{pos}")



FA.close()