'''
Bank Account Manager
Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
'''
from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdrawal(self):
        pass

    @abstractmethod
    def balance(self):
        pass


class CheckingAccount(Account):

    def __init__(self, id):
        self.total_balance = 3000
        self.id = id

    def deposit(self, amount):
        try:
            self.total_balance += amount

        except TypeError:
            print("error input")

    def withdrawal(self, amount):
        try:
            if amount <= self.total_balance:
                self.total_balance -= amount

            else:
                print("not enough balance")

        except TypeError:
            print("error input")

    def balance(self):
        print("Balance: {}".format(self.total_balance))


class SavingsAccount(Account):

    def __init__(self, id):
        self.total_balance = 2120
        self.id = id

    def deposit(self, amount):
        self.total_balance += amount

    def withdrawal(self, amount):

        if amount <= self.total_balance:
            self.total_balance -= amount

        else:
            print("not enough balance")

    def balance(self):
        print("Balance: {}".format(self.total_balance))


class BusinessAccount(Account):

    def __init__(self, id):
        self.total_balance = 40311
        self.id = id

    def deposit(self, amount):
        self.total_balance += amount

    def withdrawal(self, amount):

        if amount <= self.total_balance:
            self.total_balance -= amount

        else:
            print("not enough balance")

    def balance(self):
        print("Balance: {}".format(self.total_balance))
