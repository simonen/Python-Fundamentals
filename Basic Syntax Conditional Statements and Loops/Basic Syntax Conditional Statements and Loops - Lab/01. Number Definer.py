number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small positive")
    elif 1 <= number <= 1000000:
        print("positive")
    elif number > 1000000:
        print("large positive")
elif number < 0:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) <= 1000000:
        print("negative")
    elif abs(number) > 1000000:
        print("large negative")