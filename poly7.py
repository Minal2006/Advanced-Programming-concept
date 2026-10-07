class BankAccount:
    def calculate_interest(self, balance):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.05

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02

class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08

accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for a in accounts:
    print("Interest:", a.calculate_interest(50000))