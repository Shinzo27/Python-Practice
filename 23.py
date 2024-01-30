def check_divisibility_by_7(number):
    if number % 7 == 0:
        return True
    else:
        return False

number = int(input("Enter a number to check its divisibility by 7: "))

if check_divisibility_by_7(number):
    print(number, "is divisible by 7.")
else:
    print(number, "is not divisible by 7.")
