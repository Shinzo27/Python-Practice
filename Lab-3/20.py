# a. Function to convert date format from dd/mm/yyyy to dd-mm-yyyy
def convert_date_format(date):
    parts = date.split('/')
    new_date = '-'.join(parts)
    return new_date

# b. Function to find the number of occurrences of a specified character in a string
def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# a. Convert date format
input_date = input("Enter the date in the format (dd/mm/yyyy): ")
converted_date = convert_date_format(input_date)
print("Date in (dd-mm-yyyy) format:", converted_date)

# b. Count occurrences of a character
input_string = "hello world"
character = "l"
occurrences = count_occurrences(input_string, character)
print("Number of occurrences of '{}' in '{}': {}".format(character, input_string, occurrences))
