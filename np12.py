import numpy as np
a = np.array([10, 60, 25, 80, 45, 90, 30, 55, 20, 70])
a[a > 50] = 0
print("Array:", a)