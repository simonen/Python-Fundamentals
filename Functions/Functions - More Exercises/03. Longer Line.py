from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

a1 = abs(x1 - x2)
b1 = abs(y1 - y2)
a2 = abs(x3 - x4)
b2 = abs(y3 - y4)

if (a1 + b1) > (a2 + b2):
    if abs(x1) <= abs(x2) or abs(y1) <= abs(y2):
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
else:
    if abs(x3) <= abs(x4) or abs(y3) <= abs(y4):
        print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
    else:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")
