empl_1 = int(input())
empl_2 = int(input())
empl_3 = int(input())
students = int(input())

hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        students -= 0
    else:
        students -= (empl_3 + empl_2 + empl_1)

print(f"Time needed: {hours}h.")
