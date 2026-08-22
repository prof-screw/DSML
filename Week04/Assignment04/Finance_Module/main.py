
from Finance_Tools import calculate_tax, calculate_emi


def get_float_input(prompt):
    """Keep asking until the user provides a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.\n")


def get_int_input(prompt):
    """Keep asking until the user provides a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.\n")


def run_tax_calculator():
    print("Income Tax Calculator\n")
    income = get_float_input("Enter your annual income: ")
    try:
        tax = calculate_tax(income)
        print(f"Calculated tax: {tax}")
    except ValueError as e:
        print(f"Error: {e}")


def run_loan_calculator():
    print("Loan EMI Calculator\n")
    principal = get_float_input("Enter loan principal: ")
    rate = get_float_input("Enter annual interest rate (%): ")
    tenure = get_int_input("Enter tenure in months: ")
    try:
        emi = calculate_emi(principal, rate, tenure)
        print(f"Monthly EMI: {emi}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    print("\nFinance Tools\n")
    run_tax_calculator()
    run_loan_calculator()


if __name__ == "__main__":
    main()