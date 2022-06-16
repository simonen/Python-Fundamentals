rooms = int(input())

chairs_left = 0
is_chair_deficit = False

for room in range(1, rooms + 1):
    command = input().split(" ")
    chairs = len(command[0])
    visitors = int(command[-1])
    chair_diff = chairs - visitors
    if chair_diff >= 0:
        chairs_left += chair_diff
    else:
        print(f"{abs(chair_diff)} more chairs needed in room {room}")
        is_chair_deficit = True

if not is_chair_deficit:
    print(f"Game On, {chairs_left} free chairs left")
