budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
loaf_cost = flour_price + egg_price + milk_price * 0.25
loaf_count = 0
colored_eggs = 0
while budget > 0:
    current_budget = budget
    if current_budget <= loaf_cost:
        break
    budget -= loaf_cost
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= (loaf_count - 2)

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
