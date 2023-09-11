a = int(input("Enter your age to check eligibility, U must be over 18 to continue !!"))
if a < 18:
    print("You are not eligible Sorry Try again after",18-a,"years")
else:
    print("You are elegible to vote")
