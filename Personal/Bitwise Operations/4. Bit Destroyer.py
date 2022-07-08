def dec_bin(number_f):
    A = []
    num = int(number_f)
    while num > 0:
        A.append(str(num % 2))
        num = num // 2
    # while len(A) < 12:
    #     A.append("0")
    return A            # Reversed


def bin_dec(d):
    decim = 0
    for i in range(len(d)):
        if d[i] == "1":
            decim += (2 ** int(i))

    return decim


number = input()
binary = dec_bin(number)
print(binary[::-1])

index = int(input())
binary[index] = "0"
decimal = bin_dec(binary)

print(binary[::-1])
print(decimal)




