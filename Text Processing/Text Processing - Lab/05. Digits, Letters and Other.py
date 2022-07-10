string = input()

digits = ''
letters = ''
chars = ''

for s in string:
    if s.isdigit():
        digits += s
    elif s.isalpha():
        letters += s
    else:
        chars += s

print(digits)
print(letters)
print(chars)