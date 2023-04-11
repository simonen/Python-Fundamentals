integers = input()

A = integers.split(", ")
B = []
C = []

for num in A:
    if int(num) != 0:
        B.append(int(num))
    else:
        C.append(int(num))

print(B + C)