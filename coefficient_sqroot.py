import math
# x = (-b ± √(b^2 - 4ac)) / (2a)
a = int(input("Enter value of first coefficients"))
b = int(input("Enter value of second coefficients"))
c = int(input("Enter value of third coefficients"))

# calculating discriminant
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real and distinct roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print("One real and repeated root:")
    print("Root:", root)
else:
    print("Complex roots (no real roots):")

