from itertools import groupby

s = input().upper()
res = [''.join(g) for _, g in groupby(s, str.isdigit)]
rage = ''
uniques = ''

for i in range(0, len(res), 2):
    for char in res[i]:
        if not char.isdigit() and char not in uniques:
            uniques += char
    rage += res[i] * int(res[i + 1])

print(f"Unique symbols used: {len(uniques)}")
print(rage)
