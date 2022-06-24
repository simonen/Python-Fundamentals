chest = list(input().split("|"))
command = input()

while command != "Yohoho!":
    command = list(command.split())
    action = command[0]
    item = command[1]
    if action == "Drop" and int(item) <= len(chest) - 1:  # item = index
        dropped = chest.pop(int(item))
        chest.append(dropped)
    elif action == "Steal":  # item = count
        stolen = ", ".join(chest[-int(item):])
        print(stolen)
        chest = chest[:-int(item)]  # last 3
    elif action == "Loot":
        items = command[1::]
        chest1 = [chest.insert(0, x) for x in items if x not in chest]

    command = input()


if len(chest) == 0:
    print("Failed treasure hunt.")
else:
    total_length = len("".join(chest))
    average = total_length / len(chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
