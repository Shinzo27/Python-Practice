def concatenate_strings(str1, str2):
    result = ""
    for char in str1:
        result += char

    for char in str2:
        result += char
    return result

string1 = "Hello, "
string2 = "World!"
print(concatenate_strings(string1, string2))
