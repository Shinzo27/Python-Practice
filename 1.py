def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def main():

    boiling_point_celsius = 100

    freezing_point_celsius = 0

    boiling_point_fahrenheit = celsius_to_fahrenheit(boiling_point_celsius)
    freezing_point_fahrenheit = celsius_to_fahrenheit(freezing_point_celsius)

    print(f"Boiling point of water in Fahrenheit: {boiling_point_fahrenheit} °F")
    print(f"Freezing point of water in Fahrenheit: {freezing_point_fahrenheit} °F")

if __name__ == "__main__":
    main()

