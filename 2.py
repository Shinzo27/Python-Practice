def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    amount_payable = principal + simple_interest
    return amount_payable

def main():

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in percentage): "))
    time = float(input("Enter the time period (in years): "))

    amount_payable = calculate_simple_interest(principal, rate, time)

    print("Amount payable:", amount_payable)

if __name__ == "__main__":
    main()
