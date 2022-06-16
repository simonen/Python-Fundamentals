command = input()

A = [""] * 11

while command != "End":
    comm_args = command.split("-")
    priority = int(comm_args[0])
    note = comm_args[1]
    A.pop(priority)
    A.insert(priority, note)

    command = input()


res = [item for item in A if item != ""]
#B = []
# for i in A:
#     if i != "":
#         B.append(i)
print(res)
