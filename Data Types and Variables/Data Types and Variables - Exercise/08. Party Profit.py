group_size = int(input())
days = int(input())

day = 0
coins = 0

for day in range(1, days + 1):
    is_motivational_day = False
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coins -= 3 * group_size
        is_motivational_day = True
    if day % 5 == 0:
        coins += 20 * group_size
        if is_motivational_day:
            coins -= 2 * group_size

    coins += 50 - (2 * group_size)

print(f"{group_size} companions received {coins // group_size} coins each.")
