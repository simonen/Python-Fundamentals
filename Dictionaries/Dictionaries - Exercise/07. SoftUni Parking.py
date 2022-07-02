n = int(input())

lot = {}

for i in range(1, n + 1):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == "register":
        plate = command[2]
        if username not in lot.keys():
            lot[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif action == "unregister":
        if username not in lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            del lot[username]
            print(f"{username} unregistered successfully")

for k, v in lot.items():
    print(f"{k} => {v}")