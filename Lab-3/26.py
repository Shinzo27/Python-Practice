'''Write a program that creates a list of numbers 1–100 that are either divisible by 5 or
6.'''


for num in range(1, 101):
    if num % 5 == 0 or num % 6 == 0:
        print("Numbers from 1 to 100 that are divisible by either 5 or 6:")
        print(num)
