def calc_total_price(product, quantity):
    product_price = 0
    if product == "coffee":
        product_price = 1.5
    elif product == "water":
        product_price = 1
    elif product == "coke":
        product_price = 1.4
    elif product == "snacks":
        product_price = 2

    total_cost = product_price * quantity
    return total_cost


prod_name = input()
prod_quant = int(input())
res = calc_total_price(prod_name, prod_quant)
print(f"{res:.2f}")