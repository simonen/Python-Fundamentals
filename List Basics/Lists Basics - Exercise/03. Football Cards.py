import re

player = input()

card_list = player.split(" ")
is_Stop = False
A_list = []
B_list = []

for word in card_list:
    if re.search('[A]', word):
        (A_list.append(word))
    if re.search('[B]', word):
        B_list.append(word)
    if (11 - len(set(A_list))) < 7 or (11 - len(set(B_list))) < 7:
        is_Stop = True
        break

print(f"Team A - {11 - len(set(A_list))}; Team B - {11 - len(set(B_list))} ")
if is_Stop:
    print("Game was terminated")
