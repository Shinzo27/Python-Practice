def sum_of_series_a(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

n = int(input("Enter the value of n: "))
result_a = sum_of_series_a(n)
print("The sum of the series a is:", result_a)
