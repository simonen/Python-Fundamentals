import re

numbers = input()

match = re.finditer(r"\+359(-| )2(\1)\d{3}(\1)\d{4}\b", numbers)
res = ""

for i in match:
    match_str = i.group(0)
    res += match_str + ", "

print(res.rstrip(", "))

