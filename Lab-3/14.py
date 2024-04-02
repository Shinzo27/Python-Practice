def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def print_pascals_triangle(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=" ")
        print()

rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_pascals_triangle(rows)
