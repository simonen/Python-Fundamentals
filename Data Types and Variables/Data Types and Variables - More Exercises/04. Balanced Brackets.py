n = int(input())

balance = 1
brackets = ["(", ")"]
pair = ''

for i in range(1, n + 1):
    bracket = input()
    if bracket in brackets:
        pair += bracket
        if pair == "()":
            balance = 0
            pair = ''
        else:
            balance = 1

if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
