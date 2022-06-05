command = input()

while command != "End":
    text = command
    if text != "SoftUni":
        for t in text:
            print(t * 2, end="")
        print()
    command = input()