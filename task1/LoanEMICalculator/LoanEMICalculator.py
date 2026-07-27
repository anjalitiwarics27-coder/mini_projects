def calculate_emi(principal, annual_rate, tenure_months):
    """
    Calculate EMI (Equated Monthly Installment) for a loan.
    
    Parameters:
        principal (float): Loan amount (P)
        annual_rate (float): Annual interest rate in percent
        tenure_months (int): Loan tenure in months (N)
    
    Returns:
        float: Monthly EMI amount
    """
    # Convert annual rate (%) to monthly rate (decimal)
    monthly_rate = (annual_rate / 12) / 100

    if monthly_rate == 0:
        # Zero-interest loan: simple division
        return principal / tenure_months

    numerator = principal * monthly_rate * (1 + monthly_rate) ** tenure_months
    denominator = (1 + monthly_rate) ** tenure_months - 1
    emi = numerator / denominator
    return emi


def display_result(principal, annual_rate, tenure_months, emi):
    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    print("\n" + "=" * 40)
    print("           LOAN EMI SUMMARY")
    print("=" * 40)
    print(f"{'Principal Amount:':<22}₹{principal:,.2f}")
    print(f"{'Annual Interest Rate:':<22}{annual_rate:.2f}%")
    print(f"{'Loan Tenure:':<22}{tenure_months} months")
    print("-" * 40)
    print(f"{'Monthly EMI:':<22}₹{emi:,.2f}")
    print(f"{'Total Payment:':<22}₹{total_payment:,.2f}")
    print(f"{'Total Interest:':<22}₹{total_interest:,.2f}")
    print("=" * 40)


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 40)
    print("        LOAN EMI CALCULATOR")
    print("=" * 40)

    while True:
        principal = get_positive_float("Enter Principal Amount (₹): ")
        annual_rate = get_positive_float("Enter Annual Interest Rate (%): ")
        tenure_months = get_positive_int("Enter Loan Tenure (months): ")

        emi = calculate_emi(principal, annual_rate, tenure_months)
        display_result(principal, annual_rate, tenure_months, emi)

        again = input("\nCalculate another EMI? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using the Loan EMI Calculator!")
            break


if __name__ == "__main__":
    main()