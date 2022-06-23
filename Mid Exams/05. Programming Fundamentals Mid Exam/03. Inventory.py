items = list(input().split(", "))
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect" and item not in items:
        items.append(item)

    elif action == "Combine Items":
        item = command[1].split(":")[0]
        if item in items:
            new_item = command[1].split(":")[1]
            old_item_ind = items.index(item)
            items.insert(old_item_ind + 1, new_item)

    if action == "Drop" and item in items:
        items.remove(item)

    elif action == "Renew" and item in items:
        item_ind = items.index(item)
        renewed = items.pop(item_ind)
        items.append(renewed)

    command = input()

items = ", ".join(items)

print(items)