def smallest():
    for _ in range(1, 4):
        numbers = int(input())
        A.append(numbers)
    return min(A)


A = []
res = smallest()
print(res)