n = int(input("Enter value for n to check whether it is palindrome or not"))
orignalnumber = n
temp, reverse = 0, 0
while n != 0:
    temp += n % 10
    temp = temp * 10
    n = n // 10
reverse = temp // 10
print(reverse)
if reverse == orignalnumber:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
