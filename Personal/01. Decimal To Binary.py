def bits_count(binary_num_f, num):
    count = 0
    for i in binary_num_f:
        if i == num:
            count += 1

    return count


def binary_num(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % 2))
        num = num // 2
    #Maintain 4bit-sized chunks
    while len(A) % 4 != 0:
        A += "0"

    A = A[::-1]
    binary = ''
    for chunks in range(0, len(A), 4):
        binary += "".join(A[chunks:chunks + 4])
        if len(A[chunks::]) > 4:
            binary += " "
    return binary


command = input()
# bits = input()          # 0/1 count

while command != "stop":

    if command == "0":
        print(0)
    else:
        print(binary_num(command))

    command = input()

print((binary_num(command)))
# print(bits_count(binary_num(command), bits))