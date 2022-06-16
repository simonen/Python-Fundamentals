elect = int(input())

B = []
is_full = False

for i in range(1, 11):
    shell = 2 * i ** 2
    if elect > shell:
        elect -= shell
    else:
        shell = elect
        is_full = True
    B.insert(i, shell)
    if is_full:
        break

print(B)