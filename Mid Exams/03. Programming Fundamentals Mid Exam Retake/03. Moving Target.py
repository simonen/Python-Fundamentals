numbers = input()
command = input()

targets = list(map(int, numbers.split(" ")))

while command != "End":

    comm_list = list(command.split(" "))
    action = comm_list[0]
    index = int(comm_list[1])
    value = int(comm_list[2])

    if action == "Shoot":
        if 0 <= index <= len(targets) - 1:
            targets[index] -= value
        else:
            command = input()
            continue
        if targets[index] <= 0:
            targets.pop(index)
    elif action == "Add":
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
            command = input()
            continue
    elif action == "Strike":
        if (index + value <= len(targets) - 1) and ((index - value) >= 0):
            targets = targets[0:(index - value)] + targets[index + 1 + value::]
        else:
            print("Strike missed!")

    command = input()

result = "|".join(map(str, targets))

print(result)
