from itertools import groupby

s = input()
res = [''.join(g) for _, g in groupby(s, str.isdigit)]
rage = ''
uniques = ''

for i in range(0, len(res), 2):
    for char in res[i]:
        if not char.isdigit() and char.lower() not in uniques:
            uniques += char.lower()
    rage += res[i].upper() * int(res[i + 1])

print(f"Unique symbols used: {len(uniques)}")
print(rage)
