def calculate_sum(n):
    sum_series = 0
    for i in range(1, n+1):
        sum_series += 1 / (i ** 3)
    return sum_series

n = int(input("Enter the value of n: "))

result = calculate_sum(n)

print("The sum of the series is:", result)
