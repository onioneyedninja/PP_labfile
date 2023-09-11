my_string = "Hello, World!"

# String Length
length = len(my_string)
print(f"Length of the string: {length}")

# String Case Conversion
lowercase = my_string.lower()
uppercase = my_string.upper()
print(f"Lowercase: {lowercase}")
print(f"Uppercase: {uppercase}")

# String Splitting
split_list = my_string.split(", ")
print(f"Split List: {split_list}")

# String Replacement
replaced_string = my_string.replace("World", "Python")
print(f"Replaced String: {replaced_string}")

# String Checking
is_alpha = my_string.isalpha()
is_digit = my_string.isdigit()
is_space = my_string.isspace()
print(f"Is Alphabetical: {is_alpha}")
print(f"Is Digit: {is_digit}")
print(f"Is Space: {is_space}")

# String Formatting
name = "Prabhat"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
