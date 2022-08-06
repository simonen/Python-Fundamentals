import re

destinations = input()

match = [x[1] for x in re.findall(r"(=|\/)([A-Z][A-Za-z]{2,})\1", destinations)]

print(f"Destinations: {', '.join(match)}")
print(f"Travel Points: {len(''.join(match))}")
