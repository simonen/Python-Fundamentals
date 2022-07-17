import re

text = input()

match = re.finditer(r"(^|(?<=\s))_([a-zA-Z]*)($|(?=\s))", text)
valid = ''
for m in match:
    valid += m.group(2) + ","

print(valid.rstrip(","))