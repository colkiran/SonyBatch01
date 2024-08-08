flag = True
file = open("text1.txt", "w")
content = ''
while(flag):
    st = input("Enter the content:")
    content += st +"\n"
    Y_N = input("Do you want(Y/N): ")
    if (Y_N=="N"):
        flag = False
file.write(content)




