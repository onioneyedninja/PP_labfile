n = int(input("Enter value for n"))
temp, reverse = 0, 0
while n != 0:
    temp += n % 10
    temp = temp * 10
    n = n // 10
reverse = temp // 10
print(reverse)
