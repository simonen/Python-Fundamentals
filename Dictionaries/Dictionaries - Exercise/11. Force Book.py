command = input()

book = {}
users = []

while command != "Lumpawaroo":
    A = command.split()
    if "|" in A:
        command = command.split(" | ")
        side = command[0]
        user = command[1]

        if user in users:
            command = input()
            continue

        if side not in book.keys():
            book[side] = []
        book[side].append(user)
        users.append(user)

    elif "->" in A:
        command = command.split(" -> ")
        side = command[1]
        user = command[0]

        if user in users:
            for k, v in book.items():
                if user in v:
                    index = v.index(user)
                    v.pop(index)
        else:
            users.append(user)

        if side not in book.keys():
            book[side] = []
        book[side].append(user)

        print(f"{user} joins the {side} side!")

    command = input()

for k, v in book.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
    for member in v:
        print(f"! {member}")