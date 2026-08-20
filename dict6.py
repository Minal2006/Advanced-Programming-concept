employees = {
    101: "minu",
    102: "shreya",
    103: "Nidhi",
    104: "Gauri"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")