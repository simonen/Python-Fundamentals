entries = input()
book = {}

while not entries.isdigit():
    command = entries.split("-")
    name = command[0]
    number = command[1]
    book[name] = number

    entries = input()

for entry in range(int(entries)):
    searched_name = input()
    if searched_name in book.keys():
        print(f"{searched_name} -> {book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

# command = input()
# book = {}
#
# while True:
#     if command.isnumeric():
#         break
#     phone = command.split("-")
#     name = phone[0]
#     number = phone[1]
#     book[name] = number
#     command = input()
#
# for i in range(int(command)):
#     key = input()
#     if key in book.keys():
#         value = book[key]
#         print(f"{key} -> {value}")
#     else:
#         print(f"Contact {key} does not exist.")
