number = int(input())
A = []


def perfect(numberz):
    for numbers in range(1, numberz):
        if numberz % numbers == 0:
            A.append(numbers)

    if sum(A) == numberz:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect(number))
