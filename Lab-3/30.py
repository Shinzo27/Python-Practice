'''Describe with an example how to read and write to a text file.'''

# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, Welcome to JAIN UNIVERSITY.\n")
    file.write("It is located in Jayanagar.\n")
    file.write("This is the last line.")

# Reading from a text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)
