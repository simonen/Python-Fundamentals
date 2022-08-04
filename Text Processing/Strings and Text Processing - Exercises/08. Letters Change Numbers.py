upper = [chr(x) for x in range(65, 91)]
lower = [chr(x) for x in range(97, 123)]

b = input().split()
number = 0
numbers = []
for i in b:
    f_letter = i[0]
    number = int(i[1:len(i) - 1])
    r_letter = i[-1]
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
