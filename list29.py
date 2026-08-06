temp = [30, 32, 35, 31, 29, 36, 38, 34, 33, 37]

print("Hottest Day Temperature:", max(temp))
print("Coldest Day Temperature:", min(temp))
print("Average Temperature:", sum(temp) / len(temp))

avg = sum(temp) / len(temp)

above = 0
below = 0

for i in temp:
    if i > avg:
        above += 1
    if i < avg:
        below += 1

print("Days Above Average:", above)
print("Days Below Average:", below)