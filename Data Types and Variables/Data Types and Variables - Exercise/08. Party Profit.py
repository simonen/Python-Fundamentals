group_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    motivation = 0
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coins -= 3 * group_size
        motivation = 1
    if day % 5 == 0:
        coins += 20 * group_size
        if motivation == 1:
            coins -= 2 * group_size
    coins += 50
    coins -= 2 * group_size

coin_per_com = coins // group_size

print(f"{group_size} companions received {coin_per_com} coins each.")