number = int(input())


def tribonacci(nombre):
    last1 = 1
    last2 = 1
    current = 2
    A = [1, 1, 2]
    for i in range(1, number + 1):
        next = last1 + last2 + current
        A.append(next)
        last1 = last2
        last2 = current
        current = next
    A = " ".join(map(str, A[0:number]))
    return A


print(tribonacci(number))