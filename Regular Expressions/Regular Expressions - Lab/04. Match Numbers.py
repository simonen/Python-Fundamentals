import re

numbers = input()

match = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))", numbers)

for m in match:
    print(m.group(), end=" ")