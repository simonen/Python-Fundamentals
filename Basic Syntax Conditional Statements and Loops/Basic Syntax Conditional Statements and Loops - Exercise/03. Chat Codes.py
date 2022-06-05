n = int(input())

for m in range(1, n + 1):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif (number != 88 or number != 86) and number < 88:
        print(f"GREAT!")
    elif number > 88:
        print("Bye.")