# train = [int("0") for x in range(0, int(input()))]
wagon = [0] * int(input())

command = input()
while command != "End":
    command = command.split(" ")
    action = command[0]
    if action == "add":
        people = int(command[1])
        wagon[-1] += people
    else:
        people = int(command[2])
        index = int(command[1])
    if action == "insert":
        wagon[index] += people
    elif action == "leave":
        wagon[index] -= people

    command = input()

print(wagon)