pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())
command = input()

is_lost = False

while command != "Retire":
    status = []
    command = list(command.split())
    action = command[0]
    if action == "Status":
        for section in pirate_ship:
            if section < max_health * 0.2:
                status.append(section)
        damaged_sections = len(status)
        print(f"{damaged_sections} sections need repair.")
        command = input()
        continue

    index = int(command[1])
    if (0 <= index <= len(pirate_ship) - 1) and (0 <= index <= len(warship) - 1):
        pass
    else:
        command = input()
        continue

    if action == "Fire":
        damage = int(command[2])
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            break
        command = input()
        continue

    elif action == "Repair":
        repair = int(command[2])
        pirate_ship[index] += repair
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health
        command = input()
        continue

    end_index = int(command[2])
    if action == "Defend" and (index < end_index <= len(pirate_ship) - 1):
        damage = int(command[3])
        for section in range(index, end_index + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_lost = True
                break
    if is_lost:
        break
    command = input()
else:
    pirate_status = sum(pirate_ship)
    warship_status = sum(warship)
    print(f"Pirate ship status: {pirate_status}")
    print(f"Warship status: {warship_status}")
