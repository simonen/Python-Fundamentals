command = input()
book = {}

while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    color = command[1]
    physique = int(command[2])

    if color not in book:
        book[color] = {}   # create an empty nested dictionary placeholder for name: points
    if name not in book[color] or book[color][name] < physique :
        book[color][name] = physique

    command = input()

A = []

for k, v in book.items():
    for k1, v1 in v.items():
        a = k, k1, v1
        A.append(a)

sorted_v = sorted(A, key=lambda x: (-x[2], -len(book[x[0]])))

for i in sorted_v:
    print(f"({i[0]}) {i[1]} <-> {i[2]}")