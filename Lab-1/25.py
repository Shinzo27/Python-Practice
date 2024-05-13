def calculate_determinant(a, b, c):
    determinant = b**2 - 4 * a * c
    return determinant

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

determinant = calculate_determinant(a, b, c)

if determinant > 0:
    print("The quadratic equation has two distinct real roots.")
elif determinant == 0:
    print("The quadratic equation has one real root (repeated).")
else:
    print("The quadratic equation has two complex (non-real) roots.")

print("The determinant of the quadratic equation is:", determinant)
