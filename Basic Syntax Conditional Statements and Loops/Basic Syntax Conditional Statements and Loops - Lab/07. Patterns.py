stars = int(input())

for row in range(1, stars + 1):
    for i in range(1, row + 1):
        print("*", end="")
    print()

for row2 in range(1, stars):
    for j in range(stars - row2 + 1, 1, -1):
        print("*", end="")
    print()