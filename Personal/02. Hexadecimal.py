def hex_dec(numb):
    book = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    decim = 0
    index = len(num) - 1
    for n in num:
        if n in book:
            decim += book[n] * 16 ** index
        else:
            decim += int(n) * 16 ** index
        index -= 1
    return decim


# print(hex_dec(num))
# num = list(input())


book = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
number = int(input())
hexan = ""
rem1 = ''
while number > 0:
    rem = number % 16
    number = number // 16
    if rem in book:
        rem = book[rem]
    hexan += str(rem)

print(hexan[::-1])