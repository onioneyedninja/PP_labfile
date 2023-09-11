floors = int(input("enter numbers of floors"))
for i in range(1, floors+1):
    for j in range(0, i):
        print("*", end="")
    print()
