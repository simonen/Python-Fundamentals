n = int(input())
book = {}

for _ in range(n):
    entry = input().split("<->")
    plant = entry[0]
    rarity = int(entry[1])
    if plant not in book:
        book[plant] = []
    book[plant] = [rarity]

command = input()

while command != "Exhibition":
    action = command.split(": ")[0]
    plant = command.split(": ")[1].split(" - ")[0]
    if plant not in book:
        print("error")
        command = input()
        continue
    if action == "Rate":
        rating = int(command.split(": ")[1].split(" - ")[1])
        book[plant].append(rating)

    elif action == "Update":
        new_rarity = int(command.split(": ")[1].split(" - ")[1])
        book[plant][0] = new_rarity

    elif action == "Reset":
        book[plant] = [book[plant][0]]

    command = input()

print("Plants for the exhibition:")
for p, v in book.items():
    average = 0
    if len(book[p][1::]) > 0:
        average = sum(book[p][1::]) / len(book[p][1::])
    print(f"- {p}; Rarity: {v[0]}; Rating: {average:.2f}")
