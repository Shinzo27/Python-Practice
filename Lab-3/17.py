def strip_characters(input_str, chars_to_strip):
    result = ""
    for char in input_str:
        if char not in chars_to_strip:
            result += char
    return result

input_string = "Hello, World!"
chars_to_strip = ",!"
print(strip_characters(input_string, chars_to_strip))
