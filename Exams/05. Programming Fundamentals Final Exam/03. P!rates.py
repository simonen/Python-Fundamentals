def city_index(cities_f, city_f):
    for ind, p in enumerate(cities_f):
        if p[0] == city_f:
            return ind


command = input()

cities = []
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if not any(city in c for c in cities):
        cities.append([city, population, gold])
    else:
        cities[city_index(cities, city)][1] += population
        cities[city_index(cities, city)][2] += gold

    command = input()

command2 = input()

while command2 != "End":
    command2 = command2.split("=>")
    action = command2[0]
    town = command2[1]
    i = city_index(cities, town)
    if action == "Plunder":
        people = int(command2[2])
        gold = int(command2[3])
        cities[i][1] -= people
        cities[i][2] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[i][1] <= 0 or cities[i][2] <= 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(i)

    elif action == "Prosper":
        gold = int(command2[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[i][2] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[i][2]} gold.")

    command2 = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for c in cities:
        print(f"{c[0]} -> Population: {c[1]} citizens, Gold: {c[2]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
