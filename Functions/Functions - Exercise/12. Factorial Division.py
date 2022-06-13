def factorial(num):
    fact = 1
    for digit in range(1, num + 1):
        fact *= digit

    return fact


res = factorial(int(input())) / factorial(int(input()))

print(f"{res:.2f}")
