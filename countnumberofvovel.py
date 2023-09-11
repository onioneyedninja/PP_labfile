s = input("enter a string to count number of vowel")
counter = 0
for i in range(0, len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        counter = counter + 1

print(counter)
