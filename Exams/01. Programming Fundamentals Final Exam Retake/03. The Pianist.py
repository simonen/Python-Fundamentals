def piece_index(pieces_f, piece_f):
    for ind, p in enumerate(pieces_f):
        if p[0] == piece_f:
            return ind


def valid_check(pieces_f, piece_f):
    if any(piece_f in x for x in pieces_f):
        return True
    print(f"Invalid operation! {piece} does not exist in the collection.")


n = int(input())
pieces = []

for num in range(n):
    current = []
    entries = input().split("|")
    if entries[0] not in pieces:
        pieces.append([entries[0], entries[1], entries[2]])

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    i = piece_index(pieces, piece)
    if action == "Add":
        if any(piece in x for x in pieces):
            print(f"{piece} is already in the collection!")
        else:
            composer = command[2]
            key = command[3]
            pieces.append([piece, composer, key])
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if valid_check(pieces, piece):
            pieces.pop(i)
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = command[2]
        if valid_check(pieces, piece):
            pieces[i][2] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

for piece in pieces:
    print(f"{piece[0]} -> Composer: {piece[1]}, Key: {piece[2]}")
