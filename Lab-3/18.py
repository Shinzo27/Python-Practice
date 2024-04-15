def extract_first_n_characters(input_str, n):
    # Check if n is greater than the length of the input string
    if n >= len(input_str):
        return input_str
    else:
        # If not, return the substring from index 0 to n
        return input_str[:n]

# Example usage:
input_string = "Hello, World!"
n = 8
print(extract_first_n_characters(input_string, n))
