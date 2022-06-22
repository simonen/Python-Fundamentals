shop_list = list(input().split("!"))
command = input()

while command != "Go Shopping!":
    command = list(command.split())
    item_type = command[0]
    item = command[1]

    if item_type == "Urgent":
        if item not in shop_list:
            shop_list.insert(0, item)

    if item not in shop_list:
        command = input()
        continue

    if item_type == "Unnecessary":
        shop_list.remove(item)

    elif item_type == "Rearrange":
        shop_list.remove(item)
        shop_list.append(item)

    elif item_type == "Correct":
        new_item = command[2]
        item_index = shop_list.index(item)
        shop_list[item_index] = new_item

    command = input()

shop_list = ", ".join(shop_list)
print(shop_list)