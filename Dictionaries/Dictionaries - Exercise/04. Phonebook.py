command = input()
book = {}

while True:
    if command.isnumeric():
        break
    phone = command.split("-")
    name = phone[0]
    number = phone[1]
    book[name] = number
    command = input()

for i in range(int(command)):
    key = input()
    if key in book.keys():
        value = book[key]
        print(f"{key} -> {value}")
    else:
        print(f"Contact {key} does not exist.")

