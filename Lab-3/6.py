
def generate_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1] 
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def display_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = generate_pascals_triangle(num_rows)
display_pascals_triangle(pascals_triangle)
