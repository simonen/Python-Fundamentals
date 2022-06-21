numbers = input()
command = input()

targets = list(map(int, numbers.split(" ")))
count = 0

while command != "End":
    t_index = int(command)
    if t_index >= len(targets):
        command = input()
        continue
    curr_target = targets[t_index]
    targets[t_index] = -1
    for i, target in enumerate(targets):
        if target <= curr_target and target != -1:
            targets[i] += curr_target
        elif target > curr_target and target != -1:
            targets[i] -= curr_target
    count = targets.count(-1)
    command = input()

result = " ".join(map(str, targets))

print(f"Shot targets: {count} -> {result}")