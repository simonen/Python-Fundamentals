command = input()
coffee = 0
while command != "END":
    action = command
    if action == "coding":
        coffee += 1
    elif action == "CODING":
        coffee += 2
    elif action == "dog" or action == "cat":
        coffee += 1
    elif action == "DOG" or action == "CAT":
        coffee += 2
    elif action == "movie":
        coffee += 1
    elif action == "MOVIE":
        coffee += 2
    command = input()
if coffee > 5:
    print(f"You need extra sleep")
else:
    print(coffee)
