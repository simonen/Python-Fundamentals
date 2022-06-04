n = int(input())
water = 0
capacity = 255
for i in range(1, n + 1):
    liters = int(input())
    water += liters
    if capacity < water:
        print(f"Insufficient capacity!")
        water -= liters
print(water)