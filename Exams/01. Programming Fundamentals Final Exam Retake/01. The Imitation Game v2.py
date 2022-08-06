encrypted = input()
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        n_letters = int(command[1])
        encrypted = encrypted[n_letters::] + encrypted[:n_letters]
    elif action == "Insert":
        index = int(command[1])
        subs = command[2]
        encrypted = encrypted[:index] + subs + encrypted[index::]
    elif action == "ChangeAll":
        subs = command[1]
        replacement = command[2]
        encrypted = encrypted.replace(subs, replacement)

    command = input()

print(f"The decrypted message is: {encrypted}")
