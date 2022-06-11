numbers = input()
k = int(input())

NUM_L = numbers.split(" ")
ORDERED_L = []
CURRENT_L = NUM_L

for _ in range(0, len(NUM_L)):
    index = k % len(CURRENT_L)
    ORDERED_L.append(CURRENT_L.pop(index - 1))
    LEFT = CURRENT_L[0:index - 1]
    RIGHT = CURRENT_L[index - 1:]
    if index == 0:
        CURRENT_L = LEFT + RIGHT
    else:
        CURRENT_L = RIGHT + LEFT

f = ",".join(ORDERED_L)

print("[" + f + "]")