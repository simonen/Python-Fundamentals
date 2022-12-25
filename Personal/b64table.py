upper = [chr(x) for x in range(65, 91)]
lower = [chr(x) for x in range(97, 123)]
digits_upper = [x for x in range(0, 26)]
digits_lower = [x for x in range(26, 52)]
digits = [x for x in range(0, 10)]
digits_index = [x for x in range(52, 62)]

upper_dict = dict(zip(digits_upper, upper))
lower_dict = dict(zip(digits_lower, lower))
digits_dict = dict(zip(digits_index, digits))
chars = {62: '+', 63: "/"}

upper_dict.update(lower_dict)
upper_dict.update(digits_dict)
upper_dict.update(chars)

print(upper_dict)

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print(contents)
word = "".join(contents)
word_ascii = [ord(x) for x in word]
print(word_ascii)

octets = [f'{x:08b}' for x in word_ascii]
print(octets)
binary_conc = "".join(octets)
# print(binary_conc)


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 6):
        chunk = string_f[i:i + 6]
        grouped.append(chunk)
    return grouped


C = binary_conc
if len(C) % 6 != 0:
    C += "0" * (6 - (len(C) % 6))

A = str_splitter(C)
sextets = [int(x, 2) for x in A]
enc = [str(upper_dict[x]) for x in sextets]

print("".join(enc))

