n = int(input())
water = 0
capacity = 255
for i in range(1, n + 1):
    liters = int(input())
    if capacity < liters:
        print(f"Insufficient capacity!")
        continue
    water += liters
    capacity -= liters
print(water)