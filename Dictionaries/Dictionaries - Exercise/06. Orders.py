command = input()

prodict = {}

while command != "buy":
    products = command.split()
    key = products[0]
    price = float(products[1])
    quantity = int(products[2])
    if key not in prodict.keys():
        prodict[key] = []
        prodict[key].append(price)
        prodict[key].append(quantity)
    else:
        prodict[key][1] += quantity
        prodict[key][0] = price

    command = input()


for k, v in prodict.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")