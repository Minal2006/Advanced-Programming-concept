import numpy as np
marks = np.array([55, 70, 80, 45, 90, 65, 75, 85, 60, 95,
                  50, 72, 88, 40, 68, 78, 82, 58, 92, 63])
average = np.mean(marks)
print("Class Average:", average)
print("Marks above average:", marks[marks > average])