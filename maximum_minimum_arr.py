import numpy as np
from numpy import array

n = int(input("Enter number of elements for array(To Calculate Min and Max)"))
arr = []
for i in range(0, n):
    arr.append(int(input()))
maxx = np.max(arr)
minn = np.min(arr)
print("The highest value element in the array is", maxx)
print("The minimum value element in the array is", minn)
