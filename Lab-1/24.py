def prefix_name(name, gender):
    if gender.upper() == 'M':
        return "Mr. " + name
    elif gender.upper() == 'F':
        return "Ms. " + name
    else:
        return "Invalid gender"

name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")

prefixed_name = prefix_name(name, gender)

print("Prefixed name:", prefixed_name)
