def longest_substring(string_f, len_f):
    store = []
    prev = ''
    streak_f = ''
    for i in range(len(string_f)):
        if string_f[i] == prev:
            streak_f += string_f[i]
            if i == len(string_f) - 1 and len(streak_f) > len_f:
                store.append(streak_f)
        else:
            if len(streak_f) > len_f:
                store.append(streak_f)
            streak_f = string_f[i]

        prev = string_f[i]

    return store


a = "11100huizzzingerrrr011110000ff"

print(longest_substring(a, 1))
