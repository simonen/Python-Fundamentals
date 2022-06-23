people = int(input())
seats = list(map(int, input().split(" ")))

for i in range(len(seats)):
    if seats[i] < 4:
        diff = 4 - seats[i]
    else:
        continue
    if people >= diff:
        people -= diff
        seats[i] += diff
    else:
        seats[i] += people
        people = 0
        break

if min(seats) < 4:
    print("The lift has empty spots!")

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(" ".join(map(str, seats)))
