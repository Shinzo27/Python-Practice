def calculate_grade(percentage):
    if percentage > 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'E'


percentage = float(input("Enter the percentage of marks: "))

grade = calculate_grade(percentage)

print("The grade for", percentage, "% marks is:", grade)
