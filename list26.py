marks = [78, 85, 90, 67, 56, 88, 92, 75, 81, 69,
         95, 60, 72, 84, 79, 66, 91, 58, 87, 80]

print("Highest Marks:", max(marks))

print("Lowest Marks:", min(marks))

avg = sum(marks) / len(marks)
print("Average Marks:", avg)

above = 0
for i in marks:
    if i > avg:
        above += 1
print("Students Above Average:", above)

below = 0
for i in marks:
    if i < avg:
        below += 1
print("Students Below Average:", below)