text = list(input())
indices = []

for i, l in enumerate(text):
    if ord(l) in range(65, 91):
        indices.append(i)

print(indices)
