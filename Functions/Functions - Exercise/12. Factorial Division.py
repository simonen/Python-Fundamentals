def factorial(num):
    for digit in range(1, num):
        num *= digit

    return num


res = factorial(int(input())) / factorial(int(input()))

print(f"{res:.2f}")
