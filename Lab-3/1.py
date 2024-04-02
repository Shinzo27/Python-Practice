# Initialize variables
total = 0
current_number = 100

while current_number <= 200:
    if current_number % 2 == 0:
        total += current_number
    current_number += 1

print("The sum of even numbers between 100 and 200 is:", total)
