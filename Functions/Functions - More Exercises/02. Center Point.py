import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_point(a1, b1, a2, b2):
    if abs(a1) <= abs(a2) and abs(b1) <= abs(b2):
        return math.floor(a1), math.floor(b1)
    else:
        return math.floor(a2), math.floor(b2)


closest = closest_point(x1, y1, x2, y2)
print(closest)