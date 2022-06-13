number = int(input())
number2 = int(input())


def factorial(num):
    fact = 1
    for digit in range(1, num + 1):
        fact *= digit

    return fact


res = factorial(number) / factorial(number2)

print(f"{res:.2f}")
