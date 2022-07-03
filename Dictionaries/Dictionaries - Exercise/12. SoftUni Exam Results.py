book = {}

command = input()
lang = {}
banned = []

while command != "exam finished":
    command = command.split("-")
    name = command[0]
    language = command[1]

    if language == "banned":
        book[name] = "Banned"
        if name not in banned:
            banned.append(name)
        command = input()
        continue

    points = int(command[2])

    if name not in book.keys():
        book[name] = [language, points]

    if language not in lang.keys():
        lang[language] = 0
    if name not in banned:
        lang[language] += 1

    if book[name][0] == language and points > book[name][1]:
        book[name][1] = points

    command = input()

print("Results:")
for k, v in book.items():
    if k not in banned:
        print(f"{k} | {v[1]}")

print("Submissions:")
for k1, v1 in lang.items():
    print(f"{k1} - {v1}")