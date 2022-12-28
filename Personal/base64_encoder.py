upper = [chr(x) for x in range(65, 91)]
lower = [chr(x) for x in range(97, 123)]
index_upper = [x for x in range(0, 26)]
index_lower = [x for x in range(26, 52)]
digits = [str(x) for x in range(0, 10)]
index_digits = [x for x in range(52, 62)]


def b64_encode(input_f, b64_table_f, splitter_f):
    ascii_dec = []
    for char in input_f:
        if ord(char) < 128:
            ascii_dec.append(ord(char))
        else:
            special_char = char.encode("utf8")
            ascii_dec.extend(special_char)

    # print('ascii decimals: ', ascii_dec)
    octets = [f'{x:08b}' for x in ascii_dec]
    # print('binary octets: ', octets)
    octets_concatenated = "".join(octets)

    if len(octets_concatenated) % 6 != 0:
        octets_concatenated += "0" * (6 - (len(octets_concatenated) % 6))
    sextets = splitter_f(octets_concatenated, 6)
    # print('binary sextets: ', sextets)
    b64_dec = [int(x, 2) for x in sextets]
    # print('base64 decimals: ', b64_dec)
    b64_encoded = [str(b64_table_f[x]) for x in b64_dec]
    padding = ''

    if len(b64_encoded) % 4 != 0:
        padding = '=' * (4 - len(b64_encoded) % 4)
        b64_encoded += padding
    print('padding: ', len(padding))

    return b64_encoded


def b64_decode(input_f, b64_table_f, splitter_f):
    b64_dec = [b64_table_f[x] for x in input_f]
    sextets = [f"{x:06b}" for x in b64_dec]
    # print('sextets: ', sextets)
    sextets_conc = "".join(sextets)
    octets = splitter_f(sextets_conc, 8)
    # print('octets: ', octets)
    ascii_decimal = [int(x, 2) for x in octets]
    # print('ascii decimals: ', ascii_decimal)
    decoded_chars = [chr(x) for x in ascii_decimal if x in range(10, 128)]

    return "".join(decoded_chars)


def str_splitter(string_f, byte_size_f):
    grouped = []
    for i in range(0, len(string_f), byte_size_f):
        chunk = string_f[i:i + byte_size_f]
        grouped.append(chunk)
    return grouped


def multiline_text():
    contents = []
    while True:
        try:
            line = input("Enter string to encode: ")
            print()
            if line == "enc":
                break
        except EOFError:
            break
        #appends \n to list items to mark a new line
        if len(contents) > 0:
            contents.append('\n' + line)
        else:
            contents.append(line)
    return contents


command = input('encode or decode? ')
while True:
    print()
    if command == 'encode':
        b64_table = dict(zip(index_upper, upper))
        b64_table.update(dict(zip(index_lower, lower)))
        b64_table.update(dict(zip(index_digits, digits)))
        chars = {62: '+', 63: "/"}
        b64_table.update(chars)
        text = multiline_text()
        encoded = b64_encode("".join(text), b64_table, str_splitter)
        print()
        print('Encoded string: ', "".join(encoded))
    elif command == "decode":
        b64_table = dict(zip(upper, index_upper))
        b64_table.update(dict(zip(lower, index_lower)))
        b64_table.update(dict(zip(digits, index_digits)))
        chars = {"+": 62, "/": 63}
        b64_table.update(chars)
        text = input("Enter string to decode: ")
        decoded = b64_decode(text, b64_table, str_splitter)
        print()
        print('Decoded string: ', decoded)
    # print('base64 table: ', b64_table)
    print()
    command = input('encode or decode? ')
