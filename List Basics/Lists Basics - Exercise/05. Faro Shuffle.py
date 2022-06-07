cards = input()
shuffles = int(input())

A = cards.split(" ")
first_card = A[0]
last_card = A[-1]
truncated_list = A[1:-1]
previous_list = truncated_list

for _ in range(1, shuffles + 1):
    new_list = []
    B = previous_list[:len(previous_list) // 2]
    C = previous_list[len(previous_list) // 2:]
    for i in range(len(B)):
        new_list.append(C[i])
        new_list.append(B[i])
    previous_list = new_list

previous_list.insert(0, first_card)
previous_list.append(last_card)

print(previous_list)

# 2 3 4  5 2 6
# 5 6 7  3 7 4
#
# [5,2]