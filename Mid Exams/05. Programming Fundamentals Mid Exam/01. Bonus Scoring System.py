from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

bonus_list = []
attendances_list = []

for student in range(1, students + 1):
    attendances = int(input())
    attendances_list.append(attendances)
    if lectures > 0:
        total_bonus = ceil((attendances / lectures) * (5 + bonus))
        bonus_list.append(total_bonus)


if len(bonus_list) > 0:
    max_bonus = max(bonus_list)
    max_index = bonus_list.index(max_bonus)
    attendance = attendances_list[max_index]
else:
    max_bonus = 0
    attendance = 0


print(f"Max Bonus: {max_bonus}.")
print(bonus_list)
print(f"The student has attended {attendance} lectures.")
print(attendances_list)
