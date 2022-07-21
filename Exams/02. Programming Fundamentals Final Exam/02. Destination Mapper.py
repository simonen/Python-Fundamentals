import re

string = input()

matches = re.findall(r"(=|\/)([A-Z][a-zA-Z]{2,})(\1)", string)
points = 0
destinations = []
for m in matches:
    points += len(m[1])
    destinations.append(m[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
