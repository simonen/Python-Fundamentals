command = input()
contests = {}

while command != "end of contests":
    command = command.split(":")
    contest = command[0]
    password = command[1]
    if contest not in contests.keys():
        contests[contest] = password

    command = input()


command2 = input()
submissions = {}
students = []

while command2 != "end of submissions":
    command2 = command2.split("=>")
    contest = command2[0]
    password = command2[1]
    name = command2[2]
    score = int(command2[3])
    nscore = {contest: score}
    if contest in contests.keys() and contests[contest] == password:
        pass
    else:
        command2 = input()
        continue

    if name not in submissions.keys():
        submissions[name] = {}
    if contest not in submissions[name]:
        submissions[name] = {**nscore, **submissions[name]}

    if submissions[name][contest] < score:
        submissions[name][contest] = score
    if name not in students:
        students.append(name)

    command2 = input()

winner = ''
max_sum = 0

for s in students:
    sum_v = sum(d for d in submissions[s].values())
    if sum_v > max_sum:
        max_sum = sum_v
        winner = s

print(f"Best candidate is {winner} with total {max_sum} points.")
print("Ranking:")
for s in sorted(students, key=lambda x: x[0]):
    print(s)
    sort_scores = sorted(submissions[s].items(), key=lambda x: x[1], reverse=True)
    for i in sort_scores:
        print(f"#  {i[0]} -> {i[1]}")

