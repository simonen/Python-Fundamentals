import re

text = input()

match = re.findall(r"(?<=(\#|@))([a-zA-Z]{3,})(\1\1)([a-zA-Z]{3,})\1", text)

if len(match) > 0:
    print(f"{len(match)} word pairs found!")
else:
    print("No word pairs found!")

mirrored = []

for v in match:
    if v[1] == v[3][::-1]:
        mirrored.append(f"{v[1]} <=> {v[3]}")

if len(mirrored) > 0:
    print("The mirror words are:")
    print(", ".join(mirrored))
else:
    print("No mirror words!")
