from math import ceil


def vigenere_encode(idx_plain_f, idx_key_f, upper_f):
    cipher = list(map(lambda x, y: upper_f[(x + y) % 26], idx_key_f, idx_plain_f))
    return cipher


def vigenere_decode(idx_plain_f, idx_key_f, upper_f):
    decipher = list(map(lambda x, y: upper_f[(x - y) % 26], idx_plain_f, idx_key_f))
    return decipher


def special_symbols(res_f, plaintext_f, upper_f):
    for k in range(0, len(plaintext_f)):
        if plaintext_f[k] not in upper_f:
            res_f.insert(k, plaintext_f[k])
    return "".join(res_f)


upper = [chr(x) for x in range(65, 91)]

while True:
    command = input("encode or decode?: ")
    keyword = list(input("enter key: ").upper())
    plaintext = list(input("enter text to encode / decode: ").upper())
    ratio = ceil(len(plaintext) / len(keyword))
    keyword_repeated = keyword * ratio
    key = keyword_repeated[:len(plaintext)]
    idx_plain = [upper.index(x) for x in plaintext if x in upper]
    idx_key = [upper.index(x) for x in key]
    res = ''
    if command == "encode":
        res = vigenere_encode(idx_plain, idx_key, upper)
    elif command == "decode":
        res = vigenere_decode(idx_plain, idx_key, upper)

    print(special_symbols(res, plaintext, upper))
