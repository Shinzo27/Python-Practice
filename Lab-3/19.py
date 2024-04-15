# Function to convert milliseconds to hours, minutes, and seconds
def convert_ms_to_time(milliseconds):
    seconds = milliseconds // 1000
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

# Function to compute sales commission
def compute_commission(sales_amount, commission_rate):
    commission = sales_amount * (commission_rate / 100)
    return commission

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

milliseconds = 3723000
sales_amount = 1000
commission_rate = 5
celsius_temp = 25

# a. Convert milliseconds to hours, minutes, and seconds
hours, minutes, seconds = convert_ms_to_time(milliseconds)
print("Milliseconds converted to:", hours, "hours,", minutes, "minutes,", seconds, "seconds.")

# b. Compute sales commission
commission = compute_commission(sales_amount, commission_rate)
print("Sales commission:", commission)

# c. Convert Celsius to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print("Celsius temperature of", celsius_temp, "degrees is equivalent to", fahrenheit_temp, "degrees Fahrenheit.")
