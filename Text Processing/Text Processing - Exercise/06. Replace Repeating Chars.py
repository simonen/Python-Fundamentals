word = input()

wordset = ''
prev = ''

for w in word:
    if w != prev:
        wordset += w
    prev = w

print(wordset)

