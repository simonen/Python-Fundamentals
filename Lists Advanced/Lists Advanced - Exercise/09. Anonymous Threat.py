A = list(input().split(" "))
command = input()

while command != "3:1":
    command = command.split(" ")
    action = command[0]
    start_in = int(command[1])
    end_in = int(command[2])
    if start_in < 0:
        start_in = 0

    if action == "divide" and start_in <= len(A):
        string = A.pop(start_in)
        step = int(len(string) / end_in)
        index = start_in
        for i in range(1, end_in):
            chars = string[:step]
            A.insert(index, chars)
            index += 1
            string = string[step::]
        A.insert(index, string)

    elif action == "merge":
        if end_in >= len(A):
            end_in = len(A) - 1
        if start_in < end_in:
            for j in A[start_in:end_in]:
                A[start_in] += A.pop(start_in + 1)

    command = input()

A = " ".join(A)
print(A)
