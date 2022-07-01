command = input().split()
bakery = {}

for i in range(0, len(command), 2):
    key = command[i]
    value = command[i + 1]
    bakery[key] = int(value)

print(bakery)




