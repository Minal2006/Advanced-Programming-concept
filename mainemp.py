# main.py

from emp import gross_salary, deductions, net_salary

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

# Calculate salary
gross = gross_salary(basic, hra, da)
deduction = deductions(gross)
net = net_salary(gross, deduction)

# Display result
print("\n----- Employee Salary Details -----")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("Deductions:", deduction)
print("Net Salary:", net)