command = input()


def binary_num(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.insert(0, str(num % 2))
        num = num // 2

    rem = 4 - len(A) % 4
    if rem != 4:
        for i in range(rem):
            A.insert(0, "0")

    binary = ''
    for p in range(0, len(A), 4):
        byte_a = "".join(A[:4])
        binary += byte_a
        if len(A) > 4:
            binary += " "
        del A[:4]

    return binary


while command != "stop":
    if command == "0":
        print(0)
    else:
        print(binary_num(command))

    command = input()
