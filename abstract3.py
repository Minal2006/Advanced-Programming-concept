from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Savings Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Savings Balance:", self.balance)

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current Balance:", self.balance)

s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)

c = CurrentAccount(15000)
c.deposit(5000)
c.withdraw(4000)