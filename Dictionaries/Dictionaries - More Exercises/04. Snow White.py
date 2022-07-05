command = input()
book = {}

while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    color = command[1]
    physique = int(command[2])
    name_f = {name: physique}
    if color not in book:
        book[color] = name_f
    book[color] = {**book[color], **name_f}
    if book[color][name] < physique:
        book[color][name] = physique

    command = input()

sort_len = sorted(book.items(), key=lambda x: len(x[1]), reverse=True)
A = []

for element in sort_len:
    for k, v in element[1].items():
        a = element[0], k, v
        A.append(a)

sort_physique = sorted(A, key=lambda x: x[2], reverse=True)

for i in sort_physique:
    print(f"({i[0]}) {i[1]} <-> {i[2]}")
