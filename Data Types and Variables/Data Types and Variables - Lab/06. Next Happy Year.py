years = int(input())

yearz = []

for year in range(years + 1, 100000):
    digits = year
    yearz = []
    is_unique = False
    while digits > 0:
        last_digit = digits % 10
        digits = int(digits / 10)
        if last_digit not in yearz:
            yearz.append(last_digit)
        if len(yearz) >= len(str(year)):
            yearz.reverse()
            is_unique = True
            break
    if is_unique:
        break
if len(yearz) >= len(str(year)):
    for i in yearz:
        print(i, end="")
