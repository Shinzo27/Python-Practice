def replace_string(original_str, old_str, new_str):
    result = ""
    i = 0
    while i < len(original_str):
        if original_str[i:i+len(old_str)] == old_str:
            result += new_str
            i += len(old_str)
        else:
            result += original_str[i]
            i += 1
    return result

original_string = "Hello, World!"
old_substring = "World"
new_substring = "Universe"
print(replace_string(original_string, old_substring, new_substring))
