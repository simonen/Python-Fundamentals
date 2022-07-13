char1 = input()
char2 = input()
string = input()

str_sum = 0

for char in string:
    if ord(char) in range(ord(char1) + 1, ord(char2)):
        str_sum += ord(char)

print(str_sum)