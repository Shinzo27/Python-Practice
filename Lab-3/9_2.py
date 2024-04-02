def sum_of_series_b(n):
    total = 0
    for i in range(1, n + 1):
        total += i**i / i
    return total

n = int(input("Enter the value of n: "))
result_b = sum_of_series_b(n)
print("The sum of the series b is:", result_b)
