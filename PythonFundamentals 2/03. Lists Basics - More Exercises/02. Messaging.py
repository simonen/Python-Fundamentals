digits = input().split()
text = list(input())

indices = [sum(list(map(int, list(i)))) for i in digits]
message = ''

for i in indices:
    letter = text[int(i) % len(text)]
    message += letter
    text.remove(letter)

print(message)
