string1 = list(input().split(", "))
string2 = list(input().split(", "))

C = []

for i in string1:
    for j in string2:
        if i in j and C.count(i) == 0:
            C.append(i)

print(C)