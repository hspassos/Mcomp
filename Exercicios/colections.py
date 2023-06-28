def calculate_triangle_area(vertices):
    # Extracting the vertex coordinates from the dictionary
    vertex1 = vertices[1]
    vertex2 = vertices[2]
    vertex3 = vertices[3]

    # Unpacking the coordinates into variables
    x1, y1 = vertex1
    x2, y2 = vertex2
    x3, y3 = vertex3

    # Calculating the area of the triangle using the Shoelace formula
    area = 0.5 * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

    return area

# Example usage
triangle_vertices = {
    1: (0, 0),
    2: (1, 0),
    3: (0, 2)
}

triangle_area = calculate_triangle_area(triangle_vertices)
print("The area of the triangle is:", triangle_area)