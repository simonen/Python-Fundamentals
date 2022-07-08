def binary_num(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % 2))
        num = num // 2
    while len(A) < 8:
        A.append("0")
    return A


number = input()
B = binary_num(number)
print(B[::-1])
print(B[1])


