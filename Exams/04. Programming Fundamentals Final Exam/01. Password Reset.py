password = input()
command = input()

while command != "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        password = "".join(x for i, x in enumerate(password) if i % 2 != 0)
        print(password)

    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        subs = password[index:index + length]
        password = password.replace(subs, "", 1)
        print(password)

    elif action == "Substitute":
        subs = command[1]
        new_subs = command[2]
        if subs in password:
            password = password.replace(subs, new_subs)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
