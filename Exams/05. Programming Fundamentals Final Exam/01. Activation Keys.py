import re

key = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        subs = command[1]
        if subs in key:
            print(f"{key} contains {subs}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = key[start_index:end_index]
        if case == "Upper":
            key = key[0:start_index] + substring.upper() + key[end_index::]
        elif case == "Lower":
            key = key[0:start_index] + substring.lower() + key[end_index::]
        print(key)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[0:start_index] + key[end_index::]
        print(key)

    command = input()

print(f"Your activation key is: {key}")
