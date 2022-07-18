import re

command = input()
total = 0

while command != "end of shift":
    match = re.finditer(r"%([A-Z][a-z]+)%[^$.|%]*?<([a-zA-Z0-9_]+)>[^$.|%]*?\|(\d+)\|[^$.|%]*?(\d+\.?\d*)\$", command)

    for m in match:
        name = m.group(1)
        order = m.group(2)
        quantity = int(m.group(3))
        price = float(m.group(4))
        total += price * quantity

        print(f"{name}: {order} - {(quantity * price):.2f}")

    command = input()

print(f"Total income: {total:.2f}")
