quantity = int(input())
days_left = int(input())

cost = 0
points = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:    # Ornament Set
        cost += 2 * quantity
        points += 5
    if day % 3 == 0:    # Three Skirts + Tree Garlands
        cost += (5 + 3) * quantity
        points += 3 + 10
    if day % 5 == 0:    # Tree Lights
        cost += 15 * quantity
        points += 17
        if day % 3 == 0:
            points += 30
    if day % 10 == 0:
        points -= 20
        cost += 23
        if day == days_left:
            points -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {points}")
