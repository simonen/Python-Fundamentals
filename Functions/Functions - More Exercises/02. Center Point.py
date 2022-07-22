from math import floor


def closest_point(a1, b1, a2, b2):
    if abs(a1) <= abs(a2) and abs(b1) <= abs(b2):
        return floor(a1), floor(b1)
    return floor(a2), floor(b2)


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

closest1 = closest_point(x1, y1, x2, y2)
print(closest1)
