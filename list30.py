
names = ["Atharv", "Neha", "Rahul"]
ages = [25, 30, 40]

names.append("Priya")
ages.append(28)


name = input("Enter patient name to search: ")
if name in names:
    print("Patient found")
else:
    print("Patient not found")

remove = input("Enter patient name to delete: ")
if remove in names:
    index = names.index(remove)
    names.pop(index)
    ages.pop(index)

print("Patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])


print("Total Patients:", len(names))