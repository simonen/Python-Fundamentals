n = int(input())
total = 0

for i in range(1, n + 1):
    correct = 0
    capsule_price = float(input())
    if 0.01 <= capsule_price <= 100:
        correct += 1
    days = int(input())
    if 1 <= days <= 31:
        correct += 1
    capsules = int(input())
    if 1 <= capsules <= 2000:
        correct += 1
    order = capsules * capsule_price * days
    if correct == 3:
        print(f"The price for the coffee is: ${order:.2f}")
        total += order

print(f"Total: ${total:.2f}")
