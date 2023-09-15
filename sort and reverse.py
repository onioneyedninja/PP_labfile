import numpy as np

arr = []

n = int(input("Enter number of element"))
for i in range(0, n):
    arr.append(int(input(f"Enter value of element {i+1}")))


print(arr)
print("printing sorted array",np.sort(arr))
print("printing reversed array",np.flip(arr))
