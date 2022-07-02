def average_grade(grade_list):
    count = len(grade_list)
    suma = sum(grade_list)
    average = suma / count
    return average


diary = {}

for _ in range(int(input())):
    student = input()
    grade = float(input())
    if student not in diary:
        diary[student] = []
    diary[student].append(grade)


for k, v in diary.items():
    if average_grade(v) >= 4.50:
        print(f"{k} -> {(average_grade(v)):.2f}")
