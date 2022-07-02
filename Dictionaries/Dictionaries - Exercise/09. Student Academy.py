diary = {}

for _ in range(int(input())):
    student = input()
    grade = float(input())
    if student not in diary:
        diary[student] = []
    diary[student].append(grade)

for k, v in diary.items():
    average = sum(v) / len(v)
    if average >= 4.50:
        print(f"{k} -> {average:.2f}")
