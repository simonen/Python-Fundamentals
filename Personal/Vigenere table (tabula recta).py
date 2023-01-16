upper = [chr(x) for x in range(65, 91)]
print("     ", upper)
col = 65
for i in range(0, 26):
    cipher_upper = [upper[(upper.index(x) + i) % 26] for x in upper]
    print([chr(col)], cipher_upper)
    col += 1
