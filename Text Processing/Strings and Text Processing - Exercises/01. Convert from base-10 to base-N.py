def dec_baseN(number_f, base_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % base_f))
        num = num // base_f
    A = A[::-1]
    binary = ''.join(A)

    return binary


number = input().split()
base = int(number[0])
number_convert = int(number[1])

print(dec_baseN(number_convert, base))