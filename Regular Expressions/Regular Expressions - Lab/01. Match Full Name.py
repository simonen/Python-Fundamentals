import re

s = input()

match = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", s)

print(" ".join(match))