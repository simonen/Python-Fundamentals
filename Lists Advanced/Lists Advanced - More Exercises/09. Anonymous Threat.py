A = input()
A = A.split(" ")

command = input()

while command != "3:1":
    # COMMAND BREAKDOWN
    command = command.split(" ")
    action = command[0]
    start_in = int(command[1])
    end_in = int(command[2])
    if start_in < 0:
        start_in = 0
    ###### DIVIDE
    if action == "divide":
        B = A.pop(start_in)
        step = int(len(B) / end_in)
        pos = start_in
        for i in range(1, end_in):
            substring = B[0:step]
            B = B[step::]
            A.insert(pos, substring)
            pos += 1
        if len(B) >= step:
            A.insert(pos, B)
        #print(A)
    ######## MERGE
    elif action == "merge":
        if end_in >= len(A):
            end_in = len(A) - 1
        if start_in < end_in:
            start = start_in
            for j in A[start_in:end_in]:
                A[start_in] += A.pop(start_in + 1)

    #print(A)
    command = input()

A = " ".join(A)
print(A)