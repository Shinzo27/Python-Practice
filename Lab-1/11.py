def calculate_energy(mass):
    c = 3 * 10**8  # approximately 3x10^8 m/s
    energy = mass * c**2
    return energy

mass = float(input("Enter the mass of the object in kilograms: "))

energy = calculate_energy(mass)

print("The energy equivalent of the mass", mass, "kg is", energy, "joules.")
