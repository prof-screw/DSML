def calculate_tax(income):

    if income < 0:
        raise ValueError("Income cannot be negative.")
 
    if income <= 200_000:
        return 0.0
    elif income <= 500_000:
        rate = 0.05
    elif income <= 1_000_000:
        rate = 0.20
    else:
        rate = 0.30
 
    taxable_income = income - 200_000
    return round(taxable_income * rate, 2)
