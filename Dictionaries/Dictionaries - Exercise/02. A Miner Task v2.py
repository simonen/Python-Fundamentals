command = input()

book = {}
while command != "stop":
    quantity = int(input())
    if command not in book:
        book[command] = 0
    book[command] += quantity
    command = input()

for resource, quantity in book.items():
    print(f"{resource} -> {quantity}")
