string1 = input()
string2 = input()

previous = string1

for index, digit in enumerate(string2):
    right = string1[index + 1:]
    left = string2[0:index + 1]
    current = left + right
    if current == previous:
        continue
    print(f"{left}{right}")
    previous = current

