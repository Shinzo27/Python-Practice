'''Write a function that prompts the user to enter two numbers, then invoke a function
to find the GCD of the numbers.'''

def get_two_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd():
    num1, num2 = get_two_numbers()
    result = gcd(num1, num2)
    print("The GCD of", num1, "and", num2, "is:", result)

find_gcd()
