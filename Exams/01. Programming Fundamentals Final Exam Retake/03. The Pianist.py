def valid_check(pieces_f, piece_f):
    if any(piece_f in x for x in pieces_f):
        return True
    print(f"Invalid operation! {piece} does not exist in the collection.")


def entries_add(piece_f, composer_f, key_f):
    curr = [piece_f, composer_f, key_f] # == curr.append(piece_f...)
    return curr


n = int(input())
pieces = []

for num in range(n):
    current = []
    entries = input().split("|")
    pieces.append(entries_add(entries[0], entries[1], entries[2]))

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    if action == "Add":
        if not any(piece in i for i in pieces):
            composer = command[2]
            key = command[3]
            pieces.append(entries_add(piece, composer, key))
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if valid_check(pieces, piece):
            pieces = [x for x in pieces if x[0] != piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = command[2]
        if valid_check(pieces, piece):
            for i in range(len(pieces)):
                if pieces[i][0] == piece:
                    pieces[i][2] = new_key

            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

for item in pieces:
    print(f"{item[0]} -> Composer: {item[1]}, Key: {item[2]}")
