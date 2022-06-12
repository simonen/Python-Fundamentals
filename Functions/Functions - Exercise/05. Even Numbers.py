numbers = list(map(int, input().split(" ")))


def check_even(number):
    if number % 2 == 0:
        return True

    return False


even_checks_iterator = filter(check_even, numbers)
print(list(even_checks_iterator))
