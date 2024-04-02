# Function to convert kilograms to pounds
def kg_to_pounds(kg):
    return kg * 2.20462

# Read the weight in kilograms from the user
kilograms = float(input("Enter weight in kilograms: "))

# Convert kilograms to pounds
pounds = kg_to_pounds(kilograms)

# Print the result
print("{:.2f} kilograms is equal to {:.2f} pounds.".format(kilograms, pounds))
