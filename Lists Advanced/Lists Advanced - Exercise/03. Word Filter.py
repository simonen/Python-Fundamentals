text = input().split(" ")

evens = [x for x in text if len(x) % 2 == 0]
for word in evens:
    print(word)
