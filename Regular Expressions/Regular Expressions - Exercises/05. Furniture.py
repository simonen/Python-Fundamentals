import re

command = input()
total = 0
furnitures = []

while command != "Purchase":
    match = re.findall(r">>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)(!)([0-9]+)", command)

    if len(match) > 0:
        furniture = match[0][0]
        furnitures.append(furniture)
        price = float(match[0][1])
        quantity = int(match[0][3])
        total += price * quantity

    command = input()

print(f"Bought furniture:")

for fur in furnitures:
    print(fur)

print(f"Total money spend: {total:.2f}")
