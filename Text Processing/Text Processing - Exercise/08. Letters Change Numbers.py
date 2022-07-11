# lower = [chr(x) for x in range(97, 123)]
# upper = [chr(x) for x in range(65, 91)]
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(word[1:-1]) #between first and last chars
string = input().split()
total = 0

for word in string:
    if word[0].isupper():
        total += int(word[1:-1]) / (upper.index(word[0]) + 1)
    elif word[0].islower():
        total += int(word[1:-1]) * (lower.index(word[0]) + 1)
    if word[-1].isupper():
        total -= (upper.index(word[-1]) + 1)
    elif word[-1].islower():
        total += (lower.index(word[-1]) + 1)

print(f"{total:.2f}")