key = int(input())
n = int(input())

word = ''

for i in range(1, n + 1):
    lowercase = input()
    new_lower = ord(lowercase) + key
    word += chr(new_lower)

print(f"{word}")

