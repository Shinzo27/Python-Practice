num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)