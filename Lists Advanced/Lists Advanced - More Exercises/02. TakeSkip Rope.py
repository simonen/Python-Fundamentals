string = input()

digits = [int(s) for s in string if s.isdigit()]
text = [x for x in string if not x.isdigit()]
text = "".join(text)

take_list = []
skip_list = []

for i, digit in enumerate(digits):
    if i % 2 == 0:
        take_list.append(digit)
    else:
        skip_list.append(digit)

new_string = text
taken = ""

for j in range(0, len(take_list)):
    take = new_string[0:take_list[j]]
    taken += take
    new_string = new_string[take_list[j]::]
    new_string = new_string[skip_list[j]::]

print("".join(taken))

