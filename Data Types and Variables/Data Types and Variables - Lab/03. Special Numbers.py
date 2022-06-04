n = int(input())
special = [5, 7, 11]

for i in range(1, n + 1):
    sum = 0
    digits = i
    while digits > 0:
        sum += digits % 10
        digits = int(digits / 10)
    if sum in special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
