list1 = [10, 20, 30, 40, 50]

left = list1[1:] + [list1[0]]
print("Left Rotation:", left)


right = [list1[-1]] + list1[:-1]
print("Right Rotation:", right)