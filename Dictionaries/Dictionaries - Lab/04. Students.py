students = {}
course = []

while True:

    student = input().split(":")
    if len(student) == 1:
        course = student[0].replace("_", " ")
        break

    for i in range(0, len(student), 3):
        name = student[0]
        ID = student[1]
        course = student[2]
        students[name] = ID, course

for key, value in students.items():
    if course == value[1]:
        print(f"{key} - {value[0]}")






