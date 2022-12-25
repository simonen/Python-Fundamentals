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


def b64_encode(input_f, b64_table_f, splitter_f):
    word_binary = [ord(x) for x in input_f]
    octets = [f'{x:08b}' for x in word_binary]
    binary_conc = "".join(octets)
    if len(binary_conc) % 6 != 0:
        binary_conc += "0" * (6 - (len(binary_conc) % 6))

    A = splitter_f(binary_conc)
    sextets = [int(x, 2) for x in A]
    enc = [str(b64_table_f[x]) for x in sextets]
    if len(enc) < 4:
        enc += list('=' * (4 - (len(enc))))
    return enc


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 6):
        chunk = string_f[i:i + 6]
        grouped.append(chunk)
    return grouped


contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if len(contents) > 0:
        contents.append('\n' + line)
    else:
        contents.append(line)
print(contents)

contentz = "".join(contents)
encoded = b64_encode(contentz, upper_dict, str_splitter)
print("".join(encoded))