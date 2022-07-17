import re

text = ''
for line in iter(input, text):
    text += line + " "

match = re.findall(r"\d+", text)

for m in match:
    print(m, end=" ")
