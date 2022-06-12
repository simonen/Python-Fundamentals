def round_f():
    for num in list(map(float, input().split(" "))):
        A.append(round(num))
    return A


A = []

print(round_f())