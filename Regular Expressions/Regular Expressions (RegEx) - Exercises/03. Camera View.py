import re

m, n = list(map(int, input().split()))
text = input()

match = re.findall(r"(\|<[a-zA-Z0-9]*)", text)

A = []
for i in match:
    A.append(i[2 + m:2 + m + n])

if len("".join(A)) > 0:
    print(", ".join(A))
