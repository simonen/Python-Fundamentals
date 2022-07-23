import re

text = input()

match = re.finditer(r"(?<=(\#|@))([a-zA-Z]{3,})(\1\1)([a-zA-Z]{3,})\1", text)
valid_pairs = [x.group(2) for x in match]
match2 = re.finditer(r"(?<=(\#|@))([a-zA-Z]{3,})(\1\1)([a-zA-Z]{3,})\1", text)
valid_pairs2 = [y.group(4) for y in match2]

if len(valid_pairs) > 0:
    print(f"{len(valid_pairs)} word pairs found!")
else:
    print("No word pairs found!")

mirrored = []

for i in valid_pairs:
    for x in valid_pairs2:
        if x == i[::-1]:
            mirrored.append(f"{i} <=> {x}")

if len(mirrored) > 0:
    print(f"The mirror words are:")
    print(", ".join(mirrored))
else:
    print("No mirror words!")