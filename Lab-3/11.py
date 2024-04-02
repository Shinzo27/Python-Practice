# addition
def add(a, b):
    return a + b

# subtraction
def subtract(a, b):
    return a - b

# multiplication
def multiply(a, b):
    return a * b

# division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add(num1, num2)
difference_result = subtract(num1, num2)
product_result = multiply(num1, num2)
quotient_result = divide(num1, num2)

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
