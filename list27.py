salary = [25000, 32000, 45000, 52000, 60000, 28000, 75000, 40000, 55000, 22000]

print("Highest Salary:", max(salary))

print("Lowest Salary:", min(salary))

avg = sum(salary) / len(salary)
print("Average Salary:", avg)

above = 0
for i in salary:
    if i > 50000:
        above += 1
print("Employees earning above ₹50,000:", above)

below = 0
for i in salary:
    if i < 30000:
        below += 1
print("Employees earning below ₹30,000:", below)