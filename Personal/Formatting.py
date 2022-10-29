# Splits a string into n equal parts
string = '11000000101010000000000100000101'
group_len = int(input())


def str_splitter(string_f, group_len_f):
    grouped = []
    for i in range(0, len(string_f), group_len_f):
        chunk = string_f[i:i + group_len_f]
        grouped.append(chunk)

    return grouped


res = str_splitter(string, group_len)
print(res)