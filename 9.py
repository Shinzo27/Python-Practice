import math

def sphere_volume(radius):
    # Calculate the volume of the sphere using the formula: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def main():

    radius = [7, 12, 16]

    # Calculate and display the volume of spheres with the given radii
    for radii in radius:
        volume = sphere_volume(radii)
        print(f"Volume of a sphere with radius {radii} cm:", volume)

if __name__ == "__main__":
    main()
