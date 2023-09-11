a = float(input("Enter your accurate weight in kgs"))
b = float(input("Enter your height in meters"))
bmi = a / (b * b)
if bmi < 18.5:
    remarks = "Under Weight"
elif bmi > 18.5 and bmi < 24.9:
    remarks = "Healthy"
elif bmi > 24.9 and bmi < 29.9:
    remarks = "Over weight"
else:
    remarks = "unhealthy"
print("User bmi is", bmi, "And You are", remarks)
