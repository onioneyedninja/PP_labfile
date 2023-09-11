# 1 cube + 5 cube + 3 cube is 153
n = int(input("Enter the number to check whether it is armstrong number or not"))
orignalnumber = n
temp1 = 0
while n != 0:
    temp1 += pow(n % 10, 3)
    n = n // 10

if orignalnumber == temp1:
    print("The number is armstrong number")
else:
    print("not an armstrong number")
