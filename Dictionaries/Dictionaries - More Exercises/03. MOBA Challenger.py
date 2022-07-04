command = input()
book = {}

while command != "Season end":
    command = command.split()
    player = command[0]
    action = command[1]

    if action == "->":
        position = command[2]
        skill = int(command[4])
        pos_skill = {position: skill}
        if player not in book.keys():
            book[player] = pos_skill
        book[player] = {**pos_skill, **book[player]}
        if book[player][position] < skill:
            book[player][position] = skill

    elif action == "vs":
        player2 = command[2]
        if player not in book.keys() or player2 not in book.keys():
            command = input()
            continue

        if any(i in book[player].keys() for i in book[player2].keys()):
            if sum(book[player].values()) > sum(book[player2].values()):
                del book[player2]
            else:
                del book[player]

    command = input()

individual = {}

for k, v in book.items():
    count = 0
    suma = sum(v.values())
    if k not in individual.keys():
        individual[k] = suma

sorted_a = sorted(individual.items(), key=lambda x: x[0])
sorted_v = sorted(sorted_a, key=lambda y: y[1], reverse=True)

for i in sorted_v:
    print(f"{i[0]}: {i[1]} skill")
    index = 0
    for j, d in sorted(book[i[0]].items()):
        sort_alpha = sorted(book[i[0]].items(), key=lambda x: x[0])
        sort_scores = sorted(sort_alpha, key=lambda x: x[1], reverse=True)
        print(f"- {sort_scores[index][0]} <::> {sort_scores[index][1]}")
        index += 1
