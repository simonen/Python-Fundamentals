gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()
    action = command[0]
    gift = command[1]
    if action == 'OutOfStock':
        gifts = ["None" if x == gift else x for x in gifts]
    elif action == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gifts[-1] = gift

    command = input()

gifts = [x for x in gifts if x != "None"]
print(" ".join(gifts))