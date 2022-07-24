import re

text = input()

match = re.findall(r"(\*\*|\:\:)([A-Z][a-z]{2,})(\1)", text)
digits = re.findall(r"([0-9]+)", text)
digits = "".join(digits)

# threshold = prod(map(int, digits))
threshold = 1
for d in digits:
    threshold *= int(d)

print(f"Cool threshold: {threshold}")
print(f"{len(match)} emojis found in the text. The cool ones are:")
emojis = [x[1] for x in match]
coolness = [sum(map(ord, x)) for x in emojis]

for i, e in enumerate(match):
    if coolness[i] >= threshold:
        print("".join(e))
