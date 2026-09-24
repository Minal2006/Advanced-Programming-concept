import numpy as np
a = np.array([10, 20, 30, 40, 50,60,70,80,90,100])
print("Array:", a)
print("Size:", a.size)
s=np.sum(a)
print("Sum:",s )
avg=s/10
print("average:",avg)
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
