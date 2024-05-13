def swap_numbers(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return num1, num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = swap_numbers(num1, num2)

print("After swapping (if needed):")
print("First number:", num1)
print("Second number:", num2)
