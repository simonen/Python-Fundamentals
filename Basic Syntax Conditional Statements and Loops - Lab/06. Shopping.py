budget = int(input())
command = input()

while command != "End":
    price = int(command)
    budget -= price
    if budget < 0:
        print(f"You went in overdraft!")
        break
    command = input()
else:
    print(f"You bought everything needed.")