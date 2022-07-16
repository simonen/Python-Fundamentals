import re

s = input().upper()
pattern = r"\d+"
text = "asdad3 sadsad3e4 asd6w ASas6$ W4"

match = re.findall(r"([\D+]+)(\d+)", s)
rage = ''
uniques = ''

for i in match:
    for char in i[0]:
        if not char.isdigit() and char not in uniques:
            uniques += char
    rage += i[0] * int(i[1])

print(f"Unique symbols used: {len(uniques)}")
print(rage)