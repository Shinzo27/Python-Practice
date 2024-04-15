import random

def create_random_integer_list():
    random_list = [random.randint(1, 100) for _ in range(10)]
    return random_list

# Function to separate odd and even numbers into separate lists
def separate_odd_even(input_list):
    odd_list = []
    even_list = []
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return odd_list, even_list

random_numbers = create_random_integer_list()
print("Generated Random Numbers:", random_numbers)

odd_list, even_list = separate_odd_even(random_numbers)
print("Odd Numbers:", odd_list)
print("Even Numbers:", even_list)
