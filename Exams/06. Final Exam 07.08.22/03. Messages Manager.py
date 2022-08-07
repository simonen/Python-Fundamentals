capacity = int(input())

command = input()
users = {}

while command != "Statistics":
    command = command.split("=")
    action = command[0]
    username = command[1] # => sender if action == message
    if action == "Add":
        sent = int(command[2])
        received = int(command[3])
        if username not in users:
            users[username] = [sent, received]

    elif action == "Message":
        receiver = command[2]
        if username in users and receiver in users:
            users[username][0] += 1
            curr_sender_cap = sum(users[username])
            if curr_sender_cap >= capacity:
                print(f"{username} reached the capacity!")
                del users[username]
            users[receiver][1] += 1
            curr_receiver_cap = sum(users[receiver])
            if curr_receiver_cap >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif action == "Empty":
        if username == "All":
            users = {}
        if username in users:
            del users[username]

    command = input()

print(f"Users count: {len(users.keys())}")

for k, v in users.items():
    print(f"{k} - {sum(v)}")
