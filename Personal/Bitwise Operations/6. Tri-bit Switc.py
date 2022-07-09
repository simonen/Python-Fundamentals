def joins(listf):
    J = "".join(listf)
    return J


def dec_bin(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % 2))
        num = num // 2
    # while len(A) < 12:
    #     A.append("0")
    return A            # Reversed


def bin_dec(b):
    decim = 0
    for i in range(len(b)):
        if b[i] == "1":
            decim += (2 ** int(i))

    return decim


number = input()
start = int(input())
B = dec_bin(number)

print(joins(B[::-1]))

for i, d in enumerate(B[start:start + 3]):
    if d == "1":
        B[start + i] = "0"
    elif d == "0":
        B[start + i] = "1"

print(joins(B[::-1]))
new_dec = bin_dec(B)
print(new_dec)


