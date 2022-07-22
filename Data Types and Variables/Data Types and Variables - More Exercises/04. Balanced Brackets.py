n = int(input())

brackets = ["(", ")"]
pair = ''
is_balanced = False

for i in range(1, n + 1):
    bracket = input()
    if bracket in brackets:
        pair += bracket
        if pair == "()":
            is_balanced = True
            pair = ''
        else:
            is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
