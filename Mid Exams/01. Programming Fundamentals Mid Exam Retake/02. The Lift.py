people = int(input())
curr_lift = list(map(int, input().split(" ")))

for i in range(len(curr_lift)):
    if curr_lift[i] < 4:
        diff = 4 - curr_lift[i]
        if people >= diff:
            people -= diff
            curr_lift[i] += diff
        else:
            curr_lift[i] += people
            people = 0
            break

if min(curr_lift) < 4:
    print("The lift has empty spots!")

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(" ".join(map(str, curr_lift)))
