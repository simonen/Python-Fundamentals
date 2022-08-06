n = int(input())

book = {}

for _ in range(n):
    string = input().split("|")
    piece, composer, key = string
    if piece not in book:
        book[piece] = {"Composer": composer, "Key": key}

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece not in book:
            book[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in book:
            del book[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in book:
            book[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece in book:
    print(f"{piece} -> Composer: {book[piece]['Composer']}, Key: {book[piece]['Key']}")
