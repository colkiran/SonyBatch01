import time

def time_calc(fun):
    def helper(x):
        print("calling function......")
        st=time.perf_counter()
        result = fun(x)
        et= time.perf_counter()
        print("completed execution......")

        print(f"total time taken to exec function {round(et-st,2)}")
    return helper


lst = []
@time_calc
def fun(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            lst.append(j ** 3)

fun(8500)