def abs_numbers():
    number = list(map(float, input().split(" ")))
    numbers = []

    for num in number:
        numbers.append(abs(num))

    print(numbers)


abs_numbers()
