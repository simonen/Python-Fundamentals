stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index::]

    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1::]

    elif action == "Switch":
        old_string = command[1]
        new_sting = command[2]
        stops = stops.replace(old_string, new_sting)

    print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
