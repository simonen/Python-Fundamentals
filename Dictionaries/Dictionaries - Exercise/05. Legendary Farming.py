stash = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = ["shards", "fragments", "motes"]
legend_items = ["Shadowmourne", "Valanyr", "Dragonwrath"]
legend_found = []
junk = []

while True:

    items = input().lower().split()
    for i in range(0, len(items), 2):
        key = items[i + 1]
        value = int(items[i])
        if key not in stash.keys():
            stash[key] = value
        else:
            stash[key] += value

        if key in key_materials and stash[key] >= 250:
            stash[key] = stash[key] - 250
            l_index = key_materials.index(key)
            legendary_item = legend_items[l_index]
            legend_found.append(legendary_item)
            print(f"{legend_items[l_index]} obtained!")
            break
        elif key not in key_materials and key not in junk:
            junk.append(key)

    if len(legend_found) > 0:
        break


for j in key_materials:
    if j in stash.keys():
        print(f"{j}: {stash[j]}")

for k in junk:
    if k in stash.keys():
        print(f"{k}: {stash[k]}")

