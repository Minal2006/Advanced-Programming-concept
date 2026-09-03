# Store deposits and withdrawals in a file. Read the file and calculate: 
# Total deposits 
# Total withdrawals 
# Final balance 
# Largest transaction


file = open("transactions.txt", "w")
file.write("Deposit,5000\n")
file.write("Withdrawal,1000\n")
file.write("Deposit,3000\n")
file.write("Withdrawal,500\n")
file.write("Deposit,7000\n")
file.close()
file = open("transactions.txt", "r")
total_deposits = 0
total_withdrawals = 0
balance = 0
largest_transaction = 0
for line in file:
    data = line.strip().split(",")

    transaction = data[0]
    amount = int(data[1])

    if transaction == "Deposit":
        total_deposits = total_deposits + amount
        balance = balance + amount

  
    elif transaction == "Withdrawal":
        total_withdrawals = total_withdrawals + amount
        balance = balance - amount

  
    if amount > largest_transaction:
        largest_transaction = amount

file.close()



print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest_transaction)