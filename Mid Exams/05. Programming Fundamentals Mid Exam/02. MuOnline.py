rooms = list(input().split("|"))

health = 100
bitcoin = 0
turn = 0

for room in rooms:
    turn += 1
    find = room.split()[0]
    value = int(room.split()[1])

    if find == "potion":
        if health + value > 100:
            healed = 100 - health
            health = 100
        else:
            healed = value
            health += value
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif find == "chest":
        bitcoin += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {find}.")
        else:
            print(f"You died! Killed by {find}.")
            print(f"Best room: {turn}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

