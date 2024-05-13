import math

def sphere_volume(radius):
    # Calculate the volume of the sphere using the formula: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = [7, 12, 16]
for radii in radius:
    volume = sphere_volume(radii)
    print(f"Volume of a sphere with radius {radii} cm:", volume)