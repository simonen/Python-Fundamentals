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

# print('base64 table: ', b64_table)


def b64_encode(input_f, b64_table_f, splitter_f):
    ascii_dec = [ord(x) for x in input_f]
    print('ascii decimals: ', ascii_dec)
    octets = [f'{x:08b}' for x in ascii_dec]
    print('binary octets: ', octets)
    octets_concatenated = "".join(octets)
    print('concatenated binary: ', octets_concatenated)
    if len(octets_concatenated) % 6 != 0:
        octets_concatenated += "0" * (6 - (len(octets_concatenated) % 6))

    sextets = splitter_f(octets_concatenated)
    print('binary sextets: ', sextets)
    b64_dec = [int(x, 2) for x in sextets]
    print('base64 decimals: ', b64_dec)
    b64_encoded = [str(b64_table_f[x]) for x in b64_dec]
    padding = ''
    if len(b64_encoded) % 4 != 0:
        padding = '=' * (4 - len(b64_encoded) % 4)
        b64_encoded += padding
    print('padding: ', len(padding))
    return b64_encoded


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 6):
        chunk = string_f[i:i + 6]
        grouped.append(chunk)
    return grouped


def multiline_text():
    contents = []
    while True:
        try:
            line = input()
            if line == "enc":
                break
        except EOFError:
            break
        if len(contents) > 0:
            contents.append('\n' + line)
        else:
            contents.append(line)

    return "".join(contents)


while True:
    text = multiline_text()
    encoded = b64_encode(text, b64_table, str_splitter)
    print('string length: ', len(text))
    print('encoded string: ', "".join(encoded))

