a = int(input("Enter 1 for Fahrenheit To Celsius \nEnter 2 for Celsius To Fahrenheit"))
if a == 1:
    temp = float(input("Enter value in Fahrenheit"))
    C = (temp - 32.0) * 5.0 / 9.0
    print("Value in Celsius is :", C)
elif a == 2:
    temp = float(input("Enter value in Celsius"))
    F = temp * (9 / 5) + 32
    print("Value in Fahrenheit is :", F)
else:
    print("Enter a valid input")
