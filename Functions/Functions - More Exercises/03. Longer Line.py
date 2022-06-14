import math

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
        print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
else:
    if abs(x3) <= abs(x4) or abs(y3) <= abs(y4):
        print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
    else:
        print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")
