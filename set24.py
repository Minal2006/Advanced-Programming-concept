day1 = {10, 12, 40, 50}
day2 = {40, 104, 50, 106}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)