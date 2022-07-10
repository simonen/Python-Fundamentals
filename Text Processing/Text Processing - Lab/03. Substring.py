substr = input()
text = input()

while substr in text:
    text = text.replace(substr, "")

print(text)

