import math

def calculate_height(length, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    height = length * math.sin(angle_radians)
    return height

cases = [
    {"length": 16, "angle": 75},
    {"length": 20, "angle": 0},
    {"length": 24, "angle": 45},
    {"length": 24, "angle": 80}
]

for case in cases:
    height = calculate_height(case["length"], case["angle"])
    print(f"For a ladder of length {case['length']} feet and angle {case['angle']} degrees, the height reached on the wall is {height:.2f} feet.")
