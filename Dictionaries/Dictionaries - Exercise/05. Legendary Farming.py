stash = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = ["shards", "fragments", "motes"]
legend_items = ["Shadowmourne", "Valanyr", "Dragonwrath"]
is_legend_found = False
junk = []

while True:

    items = input().lower().split()
    for i in range(0, len(items), 2):
        item = items[i + 1]
        quantity = int(items[i])
        if item not in stash.keys():
            stash[item] = quantity
        else:
            stash[item] += quantity

        if item in key_materials and stash[item] >= 250:
            stash[item] = stash[item] - 250
            l_index = key_materials.index(item)
            print(f"{legend_items[l_index]} obtained!")
            is_legend_found = True
            break
        elif item not in key_materials and item not in junk:
            junk.append(item)

    if is_legend_found:
        break

for k in key_materials:
    print(f"{k}: {stash[k]}")

for j in junk:
    print(f"{j}: {stash[j]}")
