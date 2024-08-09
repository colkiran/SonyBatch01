
from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manager's Job")


class Developer(Employee):

    def doJob(self):
        print("Developers Job")


def BankJob(emp):
    print('Bank job started.......')
    emp.doJob()
    print('Bank job ended..........')
    print("-" * 60)


mark = Manager()
dave = Developer()


BankJob(mark)           # managers job
BankJob(dave)           # developers job

