import re

text = input()

match = re.findall(r"^|(?<=\s)([a-z0-9]+[a-z0-9\-.]+[a-z0-9]@[a-z]+[a-z\-.]+\.[a-z]+)", text)

for m in match:
    print(m)
