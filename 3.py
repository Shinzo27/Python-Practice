def days_to_complete_job(x, y, z):
    days = (x * y * z) / (x * y + y * z + x * z)
    return days

x = float(input("Enter the number of days person A takes to complete the job alone: "))
y = float(input("Enter the number of days person B takes to complete the job alone: "))
z = float(input("Enter the number of days person C takes to complete the job alone: "))

total_days = days_to_complete_job(x, y, z)

print("Number of days to complete the job together:", total_days)
