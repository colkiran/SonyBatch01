
FL = open("data.txt", "r")       # defualt mode is read mode

st = FL.read()
print(st)

# st = FL.readline(900)
# print(st)
#
# st = FL.readlines(860)
# print(st)

# for line in FL.readlines():
#     print(line)


FL.close()