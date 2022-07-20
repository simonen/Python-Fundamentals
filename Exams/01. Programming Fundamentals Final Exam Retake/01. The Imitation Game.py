text1 = list(input())
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number = int(command[1])
        text1 = text1[number::] + text1[:number]

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        text1.insert(index, value)
        text1 = list("".join(text1))

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        text1 = list("".join(text1).replace(substring, replacement))

    command = input()

print(f'The decrypted message is: {"".join(text1)}')
