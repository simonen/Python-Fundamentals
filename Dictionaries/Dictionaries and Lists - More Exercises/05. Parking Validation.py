import re

n = int(input())
book = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        plate_number = command[2]
        match = re.findall(r"([A-Z]{2}[0-9]{4}[A-Z]{2})", plate_number)
        if username in book:
            print(f"ERROR: already registered with plate number {book[username]}")
            continue
        if len(match) == 0:
            print(f"ERROR: invalid license plate {plate_number}")
            continue
        if plate_number in book.values():
            print(f"ERROR: license plate {plate_number} is busy")
            continue
        book[username] = plate_number
        print(f"{username} registered {plate_number} successfully")

    elif action == "unregister":
        if username not in book.keys():
            print(f"ERROR: user {username} not found")
            continue
        del book[username]
        print(f"user {username} unregistered successfully")

for user, plate in book.items():
    print(f"{user} => {plate}")
