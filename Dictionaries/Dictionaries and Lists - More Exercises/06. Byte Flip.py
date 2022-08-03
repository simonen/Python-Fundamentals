def hex_dec(numb):
    book = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    decim = 0
    index = len(numb) - 1
    for n in numb:
        if n in book:
            decim += book[n] * 16 ** index
        else:
            decim += int(n) * 16 ** index
        index -= 1
    return decim


string = input().split()

reversed_items = [x[::-1] for x in string if len(x) == 2][::-1]
decoded = [chr(hex_dec(x)) for x in reversed_items]

print("".join(decoded))
