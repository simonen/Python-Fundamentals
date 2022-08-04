string = input()
pattern = input()
count = string.count(pattern)

while count > 1 and len(pattern) > 0:
    len_patt = len(pattern) // 2
    string = "".join(string.rsplit(pattern, 1))
    string = "".join(string.split(pattern, 1))
    pattern = pattern[0:len_patt] + pattern[len_patt + 1::]
    print("Shaked it.")

    count = string.count(pattern)

print("No shake.")
print(string)
