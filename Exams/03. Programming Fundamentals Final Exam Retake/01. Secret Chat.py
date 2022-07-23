c_message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        c_message = c_message[:index] + " " + c_message[index::]

    elif action == "Reverse":
        subs = command[1]
        if subs not in c_message:
            print("error")
            command = input()
            continue

        c_message = c_message.replace(subs, "", 1)
        c_message += subs[::-1]

    elif action == "ChangeAll":
        old_subs = command[1]
        new_subs = command[2]
        c_message = c_message.replace(old_subs, new_subs)

    print(c_message)

    command = input()

print(f"You have a new text message: {c_message}")