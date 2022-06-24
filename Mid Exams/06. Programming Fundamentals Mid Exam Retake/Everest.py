command = input()

start = 5364
goal = 8848
days = 1

while True:
    progress = int(input())
    start += progress

    if command == "Yes":
        days += 1

    if days <= 5 and start >= goal:
        print(f"Goal reached for {days} days!")
        break

    command = input()
    if (days == 5 and start < goal) or command == "END":
        print("Failed!")
        print(start)
        break
