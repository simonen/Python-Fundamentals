def char_range(a, z):
    chars = ''
    for char in range(ord(a) + 1, ord(z)):
        chars += chr(char) + " "
    return chars


first_char = input()
second_char = input()
print(char_range(first_char, second_char))