n = int(input())
book = {}

for i in range(1, n + 1):
    command = input().split()
    race = command[0]
    name = command[1]
    damage = command[2]
    health = command[3]
    armor = command[4]
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    dha = [damage, health, armor]
    if race not in book:
        book[race] = {}
    if name not in book[race]:
        book[race][name] = []
    book[race][name] = dha

# for i in sorted_n: # Reconstruct the dictionary from the sorted list
#     if i[0] not in book1:
#         book1[i[0]] = {}
#     if i[1] not in book1[i[0]]:
#         book1[i[0]][i[1]] = {}
#     book1[i[0]][i[1]] = i[2]
#     t_damage1 = 0

for k, v in book.items():
    count = len(v)
    t_damage = 0
    t_health = 0
    t_armor = 0

    for k1, v1 in v.items():
        t_damage += int(v1[0])
        t_health += int(v1[1])
        t_armor += int(v1[2])
    a_damage = t_damage / count
    a_health = t_health / count
    a_armor = t_armor / count
    print(f"{k}::({a_damage:.2f}/{a_health:.2f}/{a_armor:.2f})")

    for k2, v2 in sorted(v.items(), key=lambda x: x):
        print(f"-{k2} -> damage: {v2[0]}, health: {v2[1]}, armor: {v2[2]}")