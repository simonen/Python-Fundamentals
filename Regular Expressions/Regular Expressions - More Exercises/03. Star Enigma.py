import re

n = int(input())

key = ["s", "t", "a", "r"]
attacked = []
destroyed = []
for i in range(1, n + 1):
    string = input()
    decrypted = ''
    count = string.lower().count("s") + string.lower().count("t") + \
            string.lower().count("a") + \
            string.lower().count("r")

    for char in string:
        decrypted += chr(ord(char) - count)
    match = re.finditer(
        r"@([A-Za-z]+)[^@\-\:\!\>]*?\:(\d+)[^@\-\:\!\>]*?\!(A|D)\![^@\-\:\!\>]*?\-\>[^@\-\:\!\>]*?(\d+)", decrypted)
    for m in match:
        planet = m.group(1)
        population = m.group(2)
        if m.group(3) == "A":
            attacked.append(planet)
        elif m.group(3) == "D":
            destroyed.append(planet)
        soldiers = m.group(4)

print(f"Attacked planets: {len(attacked)}")
for a in sorted(attacked):
    print(f"-> {a}")

print(f"Destroyed planets: {len(destroyed)}")
for d in sorted(destroyed):
    print(f"-> {d}")
