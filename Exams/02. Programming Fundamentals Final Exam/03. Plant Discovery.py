def plant_index(plants_f, plant_f):
    for i, p in enumerate(plants_f):
        if p[0] == plant_f:
            return i


number = int(input())
plants = []

for _ in range(number):
    item, rarity = input().split("<->")
    if not any(item in i for i in plants):
        plants.append([item, rarity])
    else:
        plants[plant_index(plants, item)][1] = rarity

command = input()

while command != "Exhibition":
    action = command.split(": ")[0]
    plant = command.split(": ")[1].split(" - ")[0]
    if not any(plant in z for z in plants):
        print("error")
        command = input()
        continue

    if action == "Reset":
        plants[plant_index(plants, plant)] = [plant, plants[plant_index(plants, plant)][1]]

    elif action == "Update":
        new_rarity = command.split(": ")[1].split(" - ")[1]
        plants[plant_index(plants, plant)][1] = new_rarity

    elif action == "Rate":
        rating = command.split(": ")[1].split(" - ")[1]
        plants[plant_index(plants, plant)].append(rating)
    else:
        print("error")

    command = input()

print("Plants for the exhibition:")

for i, k in enumerate(plants):
    if len(k[2::]) > 0:
        average = sum(map(float, k[2::])) / len(k[2::])
    else:
        average = 0

    print(f"- {k[0]}; Rarity: {k[1]}; Rating: {average:.2f}")
