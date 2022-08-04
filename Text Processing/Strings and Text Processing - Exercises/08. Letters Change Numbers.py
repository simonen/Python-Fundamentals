import re

upper = [chr(x) for x in range(65, 91)]
lower = [chr(x) for x in range(97, 123)]

b = input().split()
number = 0
numbers = []
for i in b:
    match = re.findall(r"([a-zA-Z])([0-9]+)([a-zA-Z])", i)
    f_letter = match[0][0]
    number = int(match[0][1])
    r_letter = match[0][2]
    if f_letter.isupper():
        number /= (upper.index(f_letter) + 1)
    elif f_letter.lower():
        number *= (lower.index(f_letter) + 1)
    if r_letter.isupper():
        number -= (upper.index(r_letter) + 1)
    elif r_letter.lower():
        number += (lower.index(r_letter) + 1)
    numbers.append(number)
    number = 0

print(f"{sum(numbers):.2f}")
