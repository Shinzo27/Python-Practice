def generate_pattern(n):
    for i in range(1, n + 1):
        pattern = ''.join(str(j) for j in range(i, 0, -1))
        print(pattern)

n = int(input("Enter the number of rows for the pattern: "))
generate_pattern(n)
