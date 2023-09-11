s = input("Enter a string to reverse")
n = len(s) - 1
# j = s[::-1]
#
# print(j)
j = ""
for i in s:
    j = i + j
print(j)
