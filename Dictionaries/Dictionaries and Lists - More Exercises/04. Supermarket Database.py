command = input()

book = {}
total = 0
while command != "stocked":
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in book:
        book[product] = {"Price": price, "Quantity": 0}
    book[product]["Price"] = price
    book[product]["Quantity"] += quantity

    command = input()

for k, v in book.items():
    print(f"{k}: ${(book[k]['Price']):.2f} * {book[k]['Quantity']} = ${(book[k]['Price'] * book[k]['Quantity']):.2f}")
    total += book[k]['Price'] * book[k]['Quantity']
print("------------------------------")
print(f"Grand Total: ${total:.2f}")
