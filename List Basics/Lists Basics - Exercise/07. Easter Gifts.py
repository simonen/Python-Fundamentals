gifts = input()
command = input()

gift_list = gifts.split(" ")

while command != "No Money":

    com = command.split()
    gift = com[1]
    commanda = com[0]
    if len(com) == 3:
        given_index = int(com[2])
        length = len(gift_list)
        if 0 <= given_index < length:
            gift_list.pop(given_index)
            gift_list.insert(given_index, gift)
    if commanda == "OutOfStock":
        for _ in range(len(gift_list)):
            if gift in gift_list:
                g_index = gift_list.index(gift)
                gift_list.pop(g_index)
                gift_list.insert(g_index, "None")
    elif commanda == "JustInCase":
        gift_list.pop()
        gift_list.append(gift)
    command = input()

for _ in range(len(gift_list)):
    if "None" in gift_list:
        g_index = gift_list.index("None")
        gift_list.pop(g_index)

print(" ".join(gift_list))