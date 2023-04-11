digits = list(map(int, input().split(", ")))
zeroz = [0 for x in range(0, digits.count(0))]
non_zeroes = [x for x in digits if x != 0]
non_zeroes.extend(zeroz)
print(non_zeroes)

# Variant 2
for i in digits:
    if i == 0:
        digits.remove(i)
        digits.append(i)

print(digits)