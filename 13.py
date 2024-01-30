def check_eligibility(name, age):
    if age >= 18:
        return f"{name}, you are eligible to apply for a driving license."
    else:
        return f"Sorry {name}, you are not eligible to apply for a driving license yet."

name = input("Enter your name: ")
age = int(input("Enter your age: "))

message = check_eligibility(name, age)
print(message)
