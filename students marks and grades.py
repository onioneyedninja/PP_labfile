a = int(input("Enter Your Marks"))
if a <= 32:
    print("f")
elif a >= 33 and a <= 49:
    print("d")
elif a >= 50 and a <= 70:
    print("c")
elif a >= 71 and a <= 85:
    print("b")
elif a >= 86 and a <= 95:
    print("a")
elif a >= 95 and a <= 100:
    print("ACE")
else:
    print("enter a valid input")
