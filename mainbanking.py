# main.py

from banking.account import create_account, check_balance
from banking.transaction import deposit, withdraw
from banking.loan import loan_calculation

# Account creation
name = input("Enter account holder name: ")
account_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = create_account(name, account_no, balance)

print("\n----- Account Details -----")
print("Name:", account["name"])
print("Account Number:", account["account_no"])
print("Balance:", check_balance(account))

# Deposit
amount = float(input("\nEnter deposit amount: "))
deposit(account, amount)
print("Balance after deposit:", check_balance(account))

# Withdrawal
amount = float(input("\nEnter withdrawal amount: "))
withdraw(account, amount)
print("Balance after withdrawal:", check_balance(account))

# Loan calculation
principal = float(input("\nEnter loan amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter loan period in years: "))

interest, total = loan_calculation(principal, rate, time)

print("\n----- Loan Details -----")
print("Loan Amount:", principal)
print("Interest:", interest)
print("Total Amount:", total)