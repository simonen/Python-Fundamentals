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

    A = A[::-1]
    return A


command = input()
bits = input()      # 0/1 count

print("".join(binary_num(command)))
print(bits_count(binary_num(command), bits))