def calculate_emi(principal, annual_interest_rate, tenure_months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_installments = tenure_months

    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_installments
    emi /= ((1 + monthly_interest_rate) ** total_installments - 1)

    total_payment = emi * total_installments
    total_interest = total_payment - principal

    return emi, total_payment, total_interest


principal_amount = float(input("Enter the principal loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
tenure_years = float(input("Enter the loan tenure in years: "))

tenure_months = int(tenure_years * 12)

emi, total_payment, total_interest = calculate_emi(principal_amount, annual_interest_rate, tenure_months)

print("\nEMI amount:", round(emi, 2))
print("Total Payment:", round(total_payment, 2))
print("Total Interest Paid:", round(total_interest, 2))
