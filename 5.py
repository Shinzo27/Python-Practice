def main():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Before swapping:")
    print("First number:", num1)
    print("Second number:", num2)

    temp = num1
    num1 = num2
    num2 = temp

    print("\nAfter swapping:")
    print("First number:", num1)
    print("Second number:", num2)

if __name__ == "__main__":
    main()