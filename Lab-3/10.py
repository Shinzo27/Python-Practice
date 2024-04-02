# Function to remove vowels from a string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

# Main program
input_string = input("Enter a string: ")
string_without_vowels = remove_vowels(input_string)
print("String after removing vowels:", string_without_vowels)
# Function to remove vowels from a string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

# Main program
input_string = input("Enter a string: ")
string_without_vowels = remove_vowels(input_string)
print("String after removing vowels:", string_without_vowels)
