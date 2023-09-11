def calculate_bill(units_consumed):
    rate1 = 3.00  # First 200 units
    rate2 = 4.50  # 201 to 400 units
    rate3 = 6.50  # Above 400 units
    # Fixed charges (monthly)
    fixed_charge = 20

    # Calculate the bill based on the consumption units
    if units_consumed <= 200:
        bill_amount = units_consumed * rate1 + fixed_charge
    elif 201 <= units_consumed <= 400:
        bill_amount = 200 * rate1 + (units_consumed - 200) * rate2 + fixed_charge
    else:
        bill_amount = 200 * rate1 + 200 * rate2 + (units_consumed - 400) * rate3 + fixed_charge

    return bill_amount


units_consumed = float(input("Enter the consumption units: "))

total_bill = calculate_bill(units_consumed)

print("Your electricity bill is: Rs.", total_bill)
