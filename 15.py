def find_min_max(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    return min_number, max_number


numbers = []
for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

min_number, max_number = find_min_max(numbers)

print("Minimum number:", min_number)
print("Maximum number:", max_number)
