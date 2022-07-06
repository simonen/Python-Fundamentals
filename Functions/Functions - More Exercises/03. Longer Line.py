from math import floor


def closest(px1, py1, px2, py2):
    if abs(px1) <= abs(px2) or abs(py1) <= abs(py2):
        return f"({floor(px1)}, {floor(py1)})({floor(px2)}, {floor(py2)})"
    return f"({floor(px2)}, {floor(py2)})({floor(px1)}, {floor(py1)})"


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input())

line1 = abs(x1 - x2) + abs(y1 - y2)
line2 = abs(x3 - x4) + abs(y3 - y4)

if line1 > line2:
    print(closest(x1, y1, x2, y2))
else:
    print(closest(x3, y3, x4, y4))
