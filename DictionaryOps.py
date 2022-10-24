a = {'Red': {'Bazgargal': ['59', '2500', '25'], 'Obsidion': ['100', '2200', '35']},
     'Black': {'Dargonax': ['200', '3500', '18']},
     'Blue': {'Kerizsa': ['60', '2100', '20'], 'Algordox': ['65', '1800', '50']}}

C = []
### Flatten out a dictionary into a list of tuples
for k, v in a.items():
    for i, p in v.items():
        tup = k, i, int(p[0]), int(p[1]), int(p[2])
        C.append(tup)

## Find the number of values belonging to a key
colors = {}
for k, v in a.items():
    if k not in colors:
        colors[k] = 0
    colors[k] = len(v)
print(colors)

# print(C)

sorted_color = sorted(C, key=lambda x: (-x[2], -len(a[x[0]])))

print(sorted_color)