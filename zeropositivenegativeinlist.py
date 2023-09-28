n = int(input("Enter number of elements in list"))
numbers = []
for i in range(0, n):
    numbers.append(int(input()))
posi_counter = 0
neg_counter = 0
zero_counter = 0
for num in numbers:
    if int(num) == 0:
        zero_counter = zero_counter + 1
    elif int(num) > 0:
        posi_counter = posi_counter + 1
    else:
        neg_counter = neg_counter + 1

print("In entered arguments there are ", posi_counter, "Positive numbers", neg_counter, "Negative numbers and",
      zero_counter, "zeros")
