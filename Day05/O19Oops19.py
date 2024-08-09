
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account.....")


    @abstractmethod
    def get_balance(self):
        pass


class Savings(Account):

    def deposit(self):
        print('deposited.......')

    def get_balance(self):
        print("The balance is #####.##")

sav = Savings()
sav.deposit()
sav.get_balance()
