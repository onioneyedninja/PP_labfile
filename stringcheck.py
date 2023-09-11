# Read user input
user_input = input("Enter a string: ")

# Check and classify the input
if user_input.isnumeric():
    print("Input is numeric.")
elif user_input.isupper():
    print("Input is in upper-case.")
elif user_input.islower():
    print("Input is in lower-case.")
else:
    print("Input is a mix of alphabetic characters and numbers.")
