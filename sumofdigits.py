n = int(input("Enter value of n"))
temp = 0
while n != 0:
    temp += n % 10
    n = n // 10

print(temp)
