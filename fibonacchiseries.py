n = int(input("Enter value of n to where u want to print fibonacci series"))
a = 0
b = 1
c = 0

print(a)
print(b)

for i in range(2, n):
    c = a + b
    a = b
    b = c
    print(b)
