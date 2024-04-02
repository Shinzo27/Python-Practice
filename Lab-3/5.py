def surface_area_of_prism(a, b, c):
    return 2 * (a * b + b * c + c * a)

a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

surface_area = surface_area_of_prism(a, b, c)

print("The surface area of the prism is:", surface_area)
