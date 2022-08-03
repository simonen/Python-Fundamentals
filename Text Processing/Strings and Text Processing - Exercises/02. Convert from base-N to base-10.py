def n_dec(numb_f, base_f):
    decimal = 0
    numb_f = numb_f[::-1]
    for i in range(len(numb_f) - 1, -1, -1):
        decimal += int(numb_f[i]) * base_f ** i

    return decimal


num = input().split()
base = int(num[0])
number = num[1]

print(n_dec(number, base))
