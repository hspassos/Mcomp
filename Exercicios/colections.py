vertices = {
    1: (0, 0),
    2: (1, 0),
    3: (0, 2)
}

def area_triangulo(vert):
    x1, y1 = vert[1]
    x2, y2 = vert[2]
    x3, y3 = vert[3]

    area = 0.5 * (x1 * (y2 -y3) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

    return area

print(area_triangulo(vertices))
