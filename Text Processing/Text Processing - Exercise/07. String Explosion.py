string = input()

power = 0
word = ""

for char in string:

    if char.isdigit():
        power += int(char)
        power -= 1
    else:
        if power == 0 or char == ">":
            word += char
        else:
            power -= 1

print(word)
