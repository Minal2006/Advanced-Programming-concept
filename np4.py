import numpy as np
a=np.arange(1,21)
even=a[a%2==0]
print(even)
odd=a[a%2!=0]
print(odd)
