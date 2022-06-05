n = int(input())

impure = [".", ",", "_"]

for i in range(1, n + 1):
    tegst = ''
    text = input()
    for t in text:
        if t not in impure:
            tegst += t
    if text == tegst:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
