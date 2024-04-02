# Function to generate the pattern
def generate_pattern(n):
    for i in range(1, n + 1):
        pattern = str(i) * i
        print(pattern)

# Main program
n = int(input("Enter the number of rows for the pattern: "))
generate_pattern(n)