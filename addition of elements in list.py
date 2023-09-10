l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l3=[]
for i in range(0, len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)
