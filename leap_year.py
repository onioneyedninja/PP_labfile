year = int(input("enter the year to check whether it was leap year or not"))
if year % 4 == 0 and year != 700:
    print("leap year")
else:
    print("Not a leap year")
