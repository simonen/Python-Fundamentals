import re

n = int(input())
digits = list(map(str, range(0, 10)))

for _ in range(n):
    string = input()
    match = re.findall(r"@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@#{1,}", string)
    group = "".join([x for x in "".join(match) if x in digits])
    if len(match) == 0:
        print("Invalid barcode")
        continue

    if len(group) == 0:
        group = "00"

    print(f"Product group: {group}")
