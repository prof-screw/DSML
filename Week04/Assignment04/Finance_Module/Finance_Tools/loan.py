def calculate_emi(principal, annual_rate, tenure_months):

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if tenure_months <= 0:
        raise ValueError("Tenure must be greater than zero months.")

    monthly_rate = annual_rate / 12 / 100

    if monthly_rate == 0:
       
        emi = principal / tenure_months
    else:
        factor = (1 + monthly_rate) ** tenure_months
        emi = principal * monthly_rate * factor / (factor - 1)

    return round(emi, 2)