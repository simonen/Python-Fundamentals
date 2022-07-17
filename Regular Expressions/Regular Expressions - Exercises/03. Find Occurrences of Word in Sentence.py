import re

text = input().lower()
string = input().lower()

match = re.findall(rf"\b{string}\b", text)

print(match.count(string))