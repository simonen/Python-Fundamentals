command = input()

total_cost = 0
is_special = False
is_regular = False

while True:
    if command == "special":
        is_special = True
        break
    elif command == "regular":
        is_regular = True
        break
    price = float(command)
    if price >= 0:
        total_cost += price
    else:
        print("Invalid price!")

    command = input()


if total_cost <= 0:
    print("Invalid order!")
else:
    before_tax = total_cost
    taxes = total_cost * 0.2
    total_cost *= 1.2  # after tax

    if is_special:
        total_cost *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {before_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_cost:.2f}$")
