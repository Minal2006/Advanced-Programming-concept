score = [45, 120, 78, 30, 150, 95, 60, 10, 105, 55]

print("Highest Score:", max(score))
print("Lowest Score:", min(score))
print("Total Runs:", sum(score))
print("Average Runs:", sum(score) / len(score))

century = 0
half = 0

for i in score:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Number of Centuries:", century)
print("Number of Half-Centuries:", half)