import math

def calculate_square_area(side):
    return side * side

def calculate_square_perimeter(side):
    return 4 * side

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

shape = input("Enter the shape (square/rectangle/triangle/circle/cylinder): ")

if shape == "square":
    side = float(input("Enter the side length of the square: "))
    print("Area of the square:", calculate_square_area(side))
    print("Perimeter of the square:", calculate_square_perimeter(side))
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of the rectangle:", calculate_rectangle_area(length, width))
    print("Perimeter of the rectangle:", calculate_rectangle_perimeter(length, width))
elif shape == "triangle":
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of the triangle:", calculate_triangle_area(base, height))
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    print("Area of the circle:", calculate_circle_area(radius))
    print("Perimeter of the circle:", calculate_circle_perimeter(radius))
elif shape == "cylinder":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    print("Surface area of the cylinder:", calculate_cylinder_surface_area(radius, height))
else:
    print("Invalid shape entered. Please enter one of: square, rectangle, triangle, circle, cylinder")
