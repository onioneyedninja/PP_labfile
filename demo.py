a = bool(input("are you 10 pass"))
if a:
  b = int(input("10 %"))
else:
  print("You are not eligible")
if b >= 60:
  c = bool(input("Subject maths and english"))
else:
  print("You are not eligible")
if c:
  print("You are eligible")
else:
  print("Youre not eligible")
