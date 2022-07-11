text = input()

previous = ""
for i in text:
    if previous == ":":
        print(previous + i)

    previous = i