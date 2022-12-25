upper = [chr(x) for x in range(65, 91)]
lower = [chr(x) for x in range(97, 123)]
index_upper = [x for x in range(0, 26)]
index_lower = [x for x in range(26, 52)]
digits = [x for x in range(0, 10)]
index_digits = [x for x in range(52, 62)]

b64_table = dict(zip(index_upper, upper))
lower_dict = dict(zip(index_lower, lower))
digits_dict = dict(zip(index_digits, digits))
chars = {62: '+', 63: "/"}

b64_table.update(lower_dict)
b64_table.update(digits_dict)
b64_table.update(chars)


def b64_encode(input_f, b64_table_f, splitter_f):
    ascii_dec = [ord(x) for x in input_f]
    octets = [f'{x:08b}' for x in ascii_dec]
    octets_concatenated = "".join(octets)
    if len(octets_concatenated) % 6 != 0:
        octets_concatenated += "0" * (6 - (len(octets_concatenated) % 6))

    sextets = splitter_f(octets_concatenated)
    b64_dec = [int(x, 2) for x in sextets]
    b64_encoded = [str(b64_table_f[x]) for x in b64_dec]
    if len(b64_encoded) < 4:
        b64_encoded += list('=' * (4 - (len(b64_encoded))))
    return b64_encoded


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 6):
        chunk = string_f[i:i + 6]
        grouped.append(chunk)
    return grouped


while True:
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
    encoded = b64_encode(contentz, b64_table, str_splitter)
    print("".join(encoded))