def create_side(book_f, side_f, user_f):
    if side_f not in book_f:
        book_f[side_f] = []
    book[side_f].append(user_f)
    return book_f


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

        create_side(book, side, user)
        users.append(user)

    elif "->" in A:
        command = command.split(" -> ")
        side = command[1]
        user = command[0]

        if user in users:
            for k, v in book.items():
                if user in v:
                    v.remove(user)
        else:
            users.append(user)

        create_side(book, side, user)
        print(f"{user} joins the {side} side!")

    command = input()

for k, v in book.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
    for member in v:
        print(f"! {member}")
