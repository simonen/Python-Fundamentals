command = input()

register = {}

while command != "End":
    command = command.split(" -> ")
    company = command[0]
    user_id = command[1]
    if company not in register.keys():
        register[company] = []
    if user_id not in register[company]:
        register[company].append(user_id)

    command = input()


for k, v in register.items():
    print(f"{k}")
    for id in v:
        print(f"-- {id}")
