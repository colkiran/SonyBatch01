def fact_number(n):
    if n == 1:
        return 1
    else:
        return n * fact_number(n-1)
print(fact_number(3))