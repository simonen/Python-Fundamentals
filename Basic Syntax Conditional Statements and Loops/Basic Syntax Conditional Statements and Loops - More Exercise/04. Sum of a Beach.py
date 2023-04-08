text = input()
words = ['sand', 'water', 'fish', 'sun']
count = 0

for word in words:
    count += text.lower().count(word)

print(count)
