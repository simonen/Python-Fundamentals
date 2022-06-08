gifts = input()
command = input()

gift_list = gifts.split(" ")

while command != "No Money":

    com_list = command.split()
    gift = com_list[1]
    if "Required" in com_list:
        given_index = int(com_list[2])
        length = len(gift_list)
        if 0 <= given_index < length:
            gift_list.pop(given_index)
            gift_list.insert(given_index, gift)
    if "OutOfStock" in com_list:
        for _ in range(len(gift_list)):
            if gift in gift_list:
                g_index = gift_list.index(gift)
                gift_list.pop(g_index)
                gift_list.insert(g_index, "None")
    elif "JustInCase" in com_list:
        gift_list.pop()
        gift_list.append(gift)
    command = input()

for _ in range(len(gift_list)):
    if "None" in gift_list:
        g_index = gift_list.index("None")
        gift_list.pop(g_index)

print(" ".join(gift_list))
