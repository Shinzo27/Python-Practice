
# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Read the temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print("{:.2f} degrees Celsius is equal to {:.2f} degrees Fahrenheit.".format(celsius, fahrenheit))
