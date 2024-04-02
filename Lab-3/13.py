def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nPr(n, r):
    return factorial(n) / factorial(n - r)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

permutations = nPr(n, r)
combinations = nCr(n, r)

print("nPr (permutations) =", permutations)
print("nCr (combinations) =", combinations)
