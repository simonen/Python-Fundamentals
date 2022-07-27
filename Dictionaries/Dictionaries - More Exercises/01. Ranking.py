command = input()
contests = {}

while command != "end of contests":
    command = command.split(":")
    contest, password = command
    if contest not in contests:
        contests[contest] = password

    command = input()

command2 = input()
submissions = {}

while command2 != "end of submissions":
    command2 = command2.split("=>")
    contest, password, username, points = command2
    if contest not in contests or password != contests[contest]:
        command2 = input()
        continue

    if username not in submissions:
        submissions[username] = {}
    if contest not in submissions[username] or submissions[username][contest] < int(points):
        submissions[username][contest] = int(points)

    command2 = input()

total_score = {}

for k, v in submissions.items():
    total_score[k] = sum(v.values())

# best_student = [x,y for x, y in total_score.items() if y == max(total_score.values())]
# print(list(total_score.keys())[list(total_score.values()).index(max(total_score.values()))])
best_student = sorted(total_score.items(), key=lambda x: -x[1])
print(f"Best candidate is {best_student[0][0]} with total {best_student[0][1]} points.")
print("Ranking:")
for user, courses in sorted(submissions.items()):
    print(user)
    for course, points in sorted(courses.items(), key=lambda y: -y[1]):
        print(f"#  {course} -> {points}")
