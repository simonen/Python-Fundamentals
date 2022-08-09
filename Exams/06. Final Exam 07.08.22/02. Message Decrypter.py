import re

n = int(input())

for _ in range(n):
    string = input()
    match = re.findall(r"^(\$|\%)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|($|\s)", string)
    if len(match) == 0:
        print("Valid message not found!")
    else:
        a = [x for x in match[0]]
        print(f"{a[1]}: {chr(int(a[2]))}{chr(int(a[3]))}{chr(int(a[4]))}")
