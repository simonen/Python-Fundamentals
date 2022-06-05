stars = int(input())

for row in range(1, stars + 1):
    for i in range(1, row + 1):
        print("*", end="")
    print()

for row2 in range(stars - 1, 0, -1):
    for j in range(0, row2):
        print("*", end="")
    print()