def sum_of_digits(number):
    sum_digits = 0
    number_str = str(number)
    for digit in number_str:
        sum_digits += int(digit)
    return sum_digits

number = int(input("Enter an integer number: "))

result = sum_of_digits(number)

print("The sum of digits of the number is:", result)
