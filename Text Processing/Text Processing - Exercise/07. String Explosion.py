string = input()

power = 0
word = ""

for char in string:
    if char.isdigit():
        power += int(char)
    if power == 0 or char == ">":
        word += char
    else:
        power -= 1

print(word)
