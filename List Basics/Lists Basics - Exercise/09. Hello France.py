items = input().split("|")
budget = float(input())

profit = 0
income = 0
expense = 0

for item in items:
    split_item = item.split("->")
    price = float(split_item[1])
    purchase = (
        ("Clothes" in item and 0.0 < price <= 50.0 and budget >= price) or
        ("Shoes" in item and 0.0 < price <= 35.0 and budget >= price) or
        ("Accessories" in item and 0.0 < price <= 20.5 and budget >= price)
    )
    if purchase:
        print(f"{(price * 1.4):.2f}", end=" ")
        income += price * 1.4
        expense += price
        budget -= price
print()
profit = income - expense

print(f"Profit: {profit:.2f}")
if budget + income >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


