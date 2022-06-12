number = int(input())
A = []


def perfect(numberz):
    for i in range(1, numberz):
        if numberz % i == 0:
            A.append(i)

    if sum(A) == numberz:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect(number))
