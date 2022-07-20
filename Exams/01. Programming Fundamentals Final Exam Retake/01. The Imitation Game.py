text = input()
command = input()
A = list(text)

while command != "Decode":

    command = command.split("|")
    action = command[0]
    if action == "Move":
        number = int(command[1])
        A = A[number::] + A[:number]

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        A.insert(index, value)
        A = list("".join(A))

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        A = list("".join(A).replace(substring, replacement))

    command = input()

print(f'The decrypted message is: {"".join(A)}')
