houses = list(map(int, input().split("@")))
command = input()

index = 0

while command != "Love!":
    command = list(command.split())
    jump = int(command[1])
    index += jump
    if index > len(houses) - 1:
        index = 0
    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        command = input()
        continue

    houses[index] -= 2
    if houses[index] == 0:
        print(f"Place {index} has Valentine's day.")

    command = input()


print(f"Cupid's last position was {index}.")

if sum(houses) == 0:
    print("Mission was successful.")
else:
    failed_houses = len(houses) - houses.count(0)
    print(f"Cupid has failed {failed_houses} places.")

