morning = {"Amit", "Atharv", "Minal", "Sneha"}
afternoon = {"Minal", "Sneha", "Ravi", "Neha"}

print("Both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one:", morning | afternoon)