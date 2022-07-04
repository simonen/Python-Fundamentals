command = input()

book = {}
users = []

while command != "no more time":
    contestant = command.split(" -> ")
    user = contestant[0]
    contest = contestant[1]
    points = int(contestant[2])
    value = {user: points}

    if contest not in book.keys():
        book[contest] = value
    book[contest] = {**value, **book[contest]}
    if book[contest][user] < points:
        book[contest][user] = points
    if user not in users:
        users.append(user)

    command = input()


students = []

for v in book.values():
    for i in v.keys():
        if i not in students:
            students.append(i)

students = sorted(students, key=lambda l: l[0])

for k, v in book.items():
    number = 1
    print(f"{k}: {len(v)} participants")
    sorted_a = sorted(book[k].items(), key=lambda x: x[0])
    sorted_v = sorted(sorted_a, key=lambda x: x[1], reverse=True)
    for w in range(len(book[k])):
        print(f"{number}. {sorted_v[w][0]} <::> {sorted_v[w][1]}")
        number += 1

print("Individual standings:")

individual = {}
for v in book.values():
    for s in students:
        if s in v.keys():
            if s not in individual:
                individual[s] = v[s]
            else:
                individual[s] += v[s]


sorted_ind = sorted(individual.items(), key=lambda y: y[0])
sorted_ind2 = sorted(sorted_ind, key=lambda t: t[1], reverse=True)
number = 1
for item in sorted_ind2:
    print(f"{number}. {item[0]} -> {item[1]}")
    number += 1
