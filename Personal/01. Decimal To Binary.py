def binary_num(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % 2))
        num = num // 2
    while len(A) % 4 != 0:
        A += "0"

    A = A[::-1]
    binary = ''
    for p in range(0, len(A), 4):
        binary += "".join(A[p:p + 4])
        if len(A) > 4:
            binary += " "

    return binary


command = input()

while command != "stop":

    if command == "0":
        print(0)
    else:
        print(binary_num(command))

    command = input()
