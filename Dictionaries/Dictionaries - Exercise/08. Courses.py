command = input()

register = {}

while command != "end":
    command = command.split(" : ")
    course = command[0]
    student = command[1]
    if course not in register.keys():
        register[course] = []
    register[course].append(student)

    command = input()

for k, v in register.items():
    print(f"{k}: {len(v)}")
    for name in v:
        print(f"-- {name}")