events = input()

A = events.split("|")
total_coins = 100
current_energy = 100

for event in A:
    info = event.split("-")
    number = int(info[-1])
    ingredient = info[0]
    if "rest" in event:
        if current_energy + number > 100:  # current = 91, number = 10,
            number = 100 - current_energy
        current_energy += number
        print(f"You gained {number} energy.")
        print(f"Current energy: {current_energy}.")
    elif "order" in event:
        if current_energy >= 30:
            total_coins += number
            current_energy -= 30
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print(f"You had to rest!")
    elif "" in event:
        if total_coins >= number:
            print(f"You bought {ingredient}.")
            total_coins -= number
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {current_energy}")
