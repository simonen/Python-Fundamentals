friends = list(input().split(", "))
command = input()

invalid = ["Blacklisted", "Lost"]
while command != "Report":
    command_list = list(command.split())
    action = command_list[0]
    index = command_list[1] #index = name in if Blacklist
    if action == "Blacklist":
        if index not in friends:
            print(f"{index} was not found.")
        else:
            name_index = friends.index(index)
            friends[name_index] = "Blacklisted"
            print(f"{index} was blacklisted.")
    elif action == "Error":
        index = int(command_list[1])
        if 0 <= index < len(friends) and friends[index] not in invalid:
            name = friends[index]
            friends[index] = "Lost"
            print(f"{name} was lost due to an error.")
    elif action == "Change":
        if 0 <= int(index) < len(friends):
            new_name = command_list[2]
            current_name = friends[int(index)]
            friends[int(index)] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    command = input()


blacklisted = friends.count("Blacklisted")
lost = friends.count("Lost")
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
friends = " ".join(friends)
print(friends)