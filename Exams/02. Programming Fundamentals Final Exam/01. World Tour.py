stops = list(input())
command = input()

while command != "Travel":
    command = command.split(":")
    action = (command[0])

    if action == "Add Stop":
        index = int(command[1])
        city = command[2]
        if 0 <= index < len(stops):
            stops.insert(index, city)
            stops = list("".join(stops))
    elif action == "Remove Stop":
        index = int(command[1])
        end_index = int(command[2])
        if (0 <= index < len(stops)) and (0 <= end_index < len(stops)):
            stops = stops[:index] + stops[end_index + 1::]

    elif action == "Switch":
        old_city = command[1]
        new_city = command[2]
        stops = list(("".join(stops)).replace(old_city, new_city))

    print(f"{''.join(stops)}")
    command = input()

print(f"Ready for world tour! Planned stops: {''.join(stops)}")
