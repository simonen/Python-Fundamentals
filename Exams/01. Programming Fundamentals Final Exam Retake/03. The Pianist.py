n = int(input())

pieces = []

for num in range(n):
    current = []
    entries = input().split("|")
    current.append(entries[0])
    current.append(entries[1])
    current.append(entries[2])
    pieces.append(current)

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    current = []
    if action == "Add":
        if not any(piece in i for i in pieces):
            composer = command[2]
            key = command[3]
            current.append(piece)
            current.append(composer)
            current.append(key)
            pieces.append(current)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if any(piece in i for i in pieces):
            pieces = [x for x in pieces if x[0] != piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if any(piece in i for i in pieces):
            for i in range(len(pieces)):
                if pieces[i][0] == piece:
                    pieces[i][2] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for item in pieces:
    print(f"{item[0]} -> Composer: {item[1]}, Key: {item[2]}")
