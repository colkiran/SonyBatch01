def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(0, 5):
    print(fibonacci(i),end=" ")
