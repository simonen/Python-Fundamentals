number = input()
new_num = ''
while len(number) > 0:
    max_digit = 0
    for digit in number:
        if int(digit) >= int(max_digit):
            max_digit = digit
    new_num += str(max_digit) * number.count(str(max_digit))
    number = number.replace(max_digit, "")

print(new_num)
