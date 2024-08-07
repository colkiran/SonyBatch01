

def outerFun(fnc):

    def helperFun(amt):
        print("Logging into the server .....")
        fnc(amt)
        print("logging out of the server......")
        print("-" * 60)

    return helperFun

@outerFun           # deposit = outerFun(deposit)
def deposit(amt):
    print(f'Amount {amt} credited successfully into account ending ####')

deposit(85000)

@outerFun
def withdraw(amt):
    print(f"Amount {amt} debited from the account ending ####")

withdraw(30000)

