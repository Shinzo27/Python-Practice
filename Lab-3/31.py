'''Write a program to read the first n lines of a file. Prompt the user to enter the value
for n.'''

def read_first_n_lines(file_name, n):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

def main():
    file_name = input("Enter the name of the file: ")
    n = int(input("Enter the number of lines to read: "))
    read_first_n_lines(file_name, n)

if __name__ == "__main__":
    main()
