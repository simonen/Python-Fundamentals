A = list(input().split(", "))
command = input()

while command != "course start":
    command = command.split(":")
    action = command[0]
    lesson_title = command[1]
    if action == "Insert" and lesson_title not in A:
        lesson_index = int(command[2])
        A.insert(lesson_index, lesson_title)

    elif action == "Swap":
        lesson2_title = command[2]
        if lesson_title in A and lesson2_title in A:
            lesson1_index = A.index(lesson_title)
            lesson2_index = A.index(lesson2_title)
            A[lesson1_index], A[lesson2_index] = A[lesson2_index], A[lesson1_index]
        for i, word in enumerate(A):
            if "-Exercise" in word:
                b = list(word.split("-"))
                lesson = b[0]
                lesson_index = A.index(lesson)
                a = A.pop(i)
                A.insert(lesson_index + 1, a)
    elif action == "Add" and lesson_title not in A:
        A.append(lesson_title)
    elif action == "Remove" and lesson_title in A:
        A.remove(lesson_title)
        for i, r in enumerate(A):
            if "-Exercise" in r and lesson_title in r:
                A.pop(i)
    elif action == "Exercise":
        if lesson_title in A:
            task_index = A.index(lesson_title)
            if A.count(lesson_title + "-Exercise") == 0:
                A.insert(task_index + 1, (lesson_title + "-Exercise"))
        elif lesson_title not in A:
            A.append(lesson_title)
            A.append(lesson_title + "-Exercise")
    command = input()

count = 1
for p in A:
    print(f"{count}.{p}")
    count += 1

