command = input()

book = {}
courses = {}

while command != "no more time":
    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if username not in book:
        book[username] = {}
    if contest not in courses:
        courses[contest] = 0
    if contest not in book[username]:
        book[username][contest] = 0
        courses[contest] += 1
    if book[username][contest] < points:
        book[username][contest] = points

    command = input()

total_score = {}

for k, v in book.items():
    total_score[k] = sum(book[k].values())

for course, participants in courses.items():
    index = 1
    print(f"{course}: {participants} participants")
    by_course = [x for x in book.items() if course in x[1]]
    for name in sorted(by_course, key=lambda x: (-x[1][course], x[0])):
        print(f"{index}. {name[0]} <::> {name[1][course]}")
        index += 1

print("Individual standings:")
index = 1
for user, score in sorted(total_score.items(), key=lambda x: (-x[1], x[0])):
    print(f"{index}. {user} -> {score}")
    index += 1
