times = input()

A = times.split(" ")
half = len(A) // 2
left_side = A[0:half]
right_side = A[half + 1:]
right_side.reverse()
left_time = 0
right_time = 0

for left in left_side:
    left_time += int(left)
    if int(left) == 0:
        left_time *= 0.8

for right in right_side:
    right_time += int(right)
    if int(right) == 0:
        right_time *= 0.8

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
