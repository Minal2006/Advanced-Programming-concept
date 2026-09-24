import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
row_sum = np.sum(a, axis=1)
column_sum = np.sum(a, axis=0)
print("Sum of each row:", row_sum)
print("Sum of each column:", column_sum)