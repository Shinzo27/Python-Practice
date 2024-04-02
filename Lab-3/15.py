def insert_in_middle(original_string, string_to_insert):
    middle_index = len(original_string) // 2
    return original_string[:middle_index] + string_to_insert + original_string[middle_index:]

# Example usage
original = "Hello World"
to_insert = "Python"
result = insert_in_middle(original, to_insert)
print("Original string:", original)
print("String to insert:", to_insert)
print("Result after insertion:", result)
