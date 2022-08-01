stash = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ''
is_found = False

while True:
    item = ''
    command = input().split()
    for i in range(0, len(command), 2):
        item = command[i + 1].lower()
        quantity = int(command[i])
        if item not in stash:
            stash[item] = 0
        stash[item] += quantity
        if stash["shards"] >= 250:
            legendary_item = "Shadowmourne"
        elif stash["fragments"] >= 250:
            legendary_item = "Valanyr"
        elif stash["motes"] >= 250:
            legendary_item = "Dragonwrath"
        if legendary_item != '':
            print(f"{legendary_item} obtained!")
            stash[item] -= 250
            is_found = True
            break

    if is_found:
        break

for item, quantity in stash.items():
    print(f"{item}: {quantity}")
