C = [x.split(":") for x in input().split()]

D = []

for i in (sorted(C, key=lambda x: int("".join(x)))):
    D.append(f"{i[0]}:{i[1]}")

print(", ".join(D))