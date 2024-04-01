def print_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = 5

print_pattern(rows)
