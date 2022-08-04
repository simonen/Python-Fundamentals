def longest_substring(string_f, subs_len_f):
    store = []
    prev = ''
    substring = ''
    for i in range(len(string_f)):
        if string_f[i] == prev:
            substring += string_f[i]
            if i == len(string_f) - 1 and len(substring) >= subs_len_f:
                store.append(substring)
        else:
            if len(substring) >= subs_len_f:
                store.append(substring)
            substring = string_f[i]

        prev = string_f[i]

    return store


a = "11100huizzzingerrrr0111100000ff"

print(longest_substring(a, 5))
