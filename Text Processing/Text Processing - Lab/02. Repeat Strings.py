text = input().split()

new_text = ""
for i in text:
    new_text += i * len(i)

print(new_text)

# print(''.join(map(lambda x: x * len(x), input().split())))