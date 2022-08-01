command = input()

minerals = {}

while command != "stop":
    key = command
    value = int(input())
    if key not in minerals.keys():
        minerals[key] = value
    else:
        minerals[key] += value

    command = input()

for k, v in minerals.items():
    print(f"{k} -> {v}")
