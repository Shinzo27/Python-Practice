def generate_sequence(n):
    sequence = []
    for i in range(1, n+1):
        if i % 2 == 0:
            sequence.append(i * 5)
        else:
            sequence.append(-(i * 5))
    return sequence

n = int(input("Enter the value of n: "))

sequence = generate_sequence(n)

print("Generated sequence:", sequence)
