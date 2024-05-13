'''Write a program to check whether an item exists within a tuple.'''

my_tuple = (10, 20, 30, 40, 50)

item_to_check = 80

if item_to_check in my_tuple:
    print("The item", item_to_check, "exists in the tuple.")
else:
    print("The item", item_to_check, "does not exist in the tuple.")
