command = input()

book = {}

while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    hat = command[1]
    size = int(command[2])

    if hat not in book:
        book[hat] = {}
    if name not in book[hat] or book[hat][name] < size:
        book[hat][name] = size

    command = input()

C = []
for hat, value in sorted(book.items(), key=lambda x: -len(x[1])):
    for name, size in value.items():
        tupl = hat, name, size
        C.append(tupl)

for i in sorted(C, key=lambda x: -x[2]):
    print(f"({i[0]}) {i[1]} <-> {i[2]}")
