pairs = input()
dict = {}

while pairs != "statistics":
    command = pairs.split(": ")
    if command[0] in dict:
        dict[command[0]] += int(command[1])
    else:
        dict[command[0]] = int(command[1])

    pairs = input()

print("Products in stock:")

for item, value in dict.items():
    print(f"- {item}: {value}")

print(f"Total Products: {len(dict)}")
print(f"Total Quantity: {sum(dict.values())}")