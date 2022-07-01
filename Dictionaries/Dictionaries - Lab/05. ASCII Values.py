letters = input().split(", ")

alpha = {letter: ord(letter) for letter in letters}

print(alpha)