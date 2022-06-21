integers = input()
command = input()

numbers = list(map(int, integers.split(" ")))

while command != "end":
    command = command.split(" ")
    action = command[0]
    if action != "decrease":
        index1 = int(command[1])
        index2 = int(command[2])
    if action == "swap":
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        numbers[index1] = numbers[index1] * numbers[index2]
    elif action == "decrease":
        for i in range(len(numbers)):
            numbers[i] -= 1

    command = input()

A = ", ".join(map(str, numbers))

print(A)
