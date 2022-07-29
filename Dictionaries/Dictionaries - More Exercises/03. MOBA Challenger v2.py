command = input()

pool = {}

while command != "Season end":
    command = command.split()
    player = command[0]
    action = command[1]
    if action == "->":
        position = command[2]
        points = int(command[4])
        if player not in pool:
            pool[player] = {}
        if position not in pool[player] or pool[player][position] < points:
            pool[player][position] = points

    elif action == "vs":
        player2 = command[2]
        if player not in pool.keys() or player2 not in pool.keys():
            command = input()
            continue

        if any(x in pool[player].keys() for x in pool[player2].keys()):
            if sum(pool[player].values()) > sum(pool[player2].values()):
                del pool[player2]
            else:
                del pool[player]

    command = input()

for k, v in sorted(pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{k}: {sum(pool[k].values())} skill")
    for pos, skill in sorted(pool[k].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {skill}")
