def calculate_compound_interest(principal, rate, time, n):
    compound_interest = principal * (1 + rate / n) ** (n * time) - principal
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal form): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times the interest is compounded per year: "))


compound_interest = calculate_compound_interest(principal, rate, time, n)

print("Compound interest:", compound_interest)
