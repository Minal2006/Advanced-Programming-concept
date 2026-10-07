class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest:", self.interest())
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(1001, 50000, 5, "Free Banking")
p.display()