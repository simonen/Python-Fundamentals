import re

names = list(input().split(", "))
book = {}
command = input()

while command != "end of race":
    points = 0
    match = re.findall(r"[a-zA-Z]+", command)
    racer = "".join(match)
    distance = sum(list(map(int, (re.findall(r"\d", command)))))
    if racer in names:
        if racer not in book:
            book[racer] = 0
        book[racer] += distance

    command = input()

winners = sorted(book.items(), key=lambda x: -x[1])

print(f"1st place: {winners[0][0]}")
print(f"2nd place: {winners[1][0]}")
print(f"3rd place: {winners[2][0]}")