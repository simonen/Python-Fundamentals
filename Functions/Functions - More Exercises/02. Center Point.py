import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
###################
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def closest_point(a1, b1, a2, b2):
    if abs(a1) <= abs(a2) and abs(b1) <= abs(b2):
        return math.floor(a1), math.floor(b1)
    else:
        return math.floor(a2), math.floor(b2)


closest1 = closest_point(x1, y1, x2, y2)
closest2 = closest_point(x3, y3, x4, y4)
print(closest1)
print(closest2)


def line_len(a1, b1, a2, b2):
    summ = abs(a1 - a2) + abs(b1 - b2)
    return summ


l_length = line_len(x1, y1, x2, y2)
print(l_length)
l_length2 = line_len(x3, y3, x4, y4)
print(l_length2)
