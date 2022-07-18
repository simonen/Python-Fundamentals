import re

text = ''
for line in iter(input, text):
    text += line + " "

match = re.findall(r"\b(www\.[a-zA-Z0-9\-.]+\.[a-z]+[\-]?[a-z0-9]+)", text)

for m in match:
    print(m)